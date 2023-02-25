import re
import os
import yaml
from pathlib import Path
from typing import Callable, Union, List, Tuple
import shutil


def normalize_path(path: Union[str, Path]):
    if isinstance(path, str):
        abs_path = os.path.abspath(path)
        return Path(abs_path)
    elif isinstance(path, Path):
        return path
    else:
        raise TypeError("Expected str or Path object")

        
def clear_folder(folder_path: Path):
    shutil.rmtree(folder_path)


def remove_empty_lines(lines: List[str]) -> List[str]:
    # remove any leading and trailing lines with only spaces
    while lines and lines[0].strip() == '':
        lines.pop(0)
    while lines and lines[-1].strip() == '':
        lines.pop()

    return lines


def parse_front_matter(lines: List[str]) -> Tuple[dict, List[str]]:
    lines = remove_empty_lines(lines)
    front_matter = {}
    content = []

    # check if the first line is the start of YAML front matter
    if lines and lines[0] == '---\n':
        # find the end of the YAML front matter (i.e., the second '---')
        try:
            fm_end_idx = lines[1:].index('---\n') + 1
        except ValueError:
            # if there is no second '---', the front matter is invalid
            raise ValueError('Invalid front matter')

        # parse the YAML front matter into a dictionary
        try:
            front_matter = yaml.safe_load(''.join(lines[1:fm_end_idx]))
        except yaml.YAMLError as e:
            raise ValueError(f'Error parsing front matter: {str(e)}')

        # get the content lines (i.e., the lines after the second '---')
        content = lines[fm_end_idx+1:]

    else:
        # if there's no front matter, treat all lines as content
        content = lines

    return front_matter, content


def add_front_matter(front_matter: dict, content: List[str]) -> List[str]:
    """This is the inverse function of parse_front_matter."""
    # convert the front matter dictionary to a YAML string
    front_matter_str = yaml.dump(front_matter, default_flow_style=False)
    md_lines = []
    # add the YAML front matter to the content
    if front_matter:
        md_lines = ['---\n']
        md_lines.extend(front_matter_str.split('\n'))
        md_lines.append('\n')
        md_lines.append('---\n')
    md_lines.extend(content)

    return md_lines


def process_math_blocks(lines: List[str]) -> List[str]:
    # Regular expression patterns for inline and display math blocks
    inline_math_pattern = r'\$(?P<math>.*?)\$'
    display_math_pattern = r'\$\$(?P<math>[\s\S]*?)\$\$'

    # Initialize list to store new lines with math blocks processed
    new_lines = []

    # Loop through each line in the input list
    in_display_math_block = False
    for line in lines:
        # Check if the line is inside a display math block
        if in_display_math_block:

            # Check if the line ends the display math block
            if '$$' in line:
                in_display_math_block = False
            # Replace asterisks with "\*" in display math block
            line = re.sub(r'(?<!\\)\*', r' * ', line)
            line = re.sub(r'(?<!\\)_', r' _ ', line)

            # Replace backslashes with double backslashes in display math block
            line = line.replace('\\', '\\\\')

        else:
            # Replace asterisks with "\*" in inline math blocks
            line = re.sub(inline_math_pattern, lambda m: "$" + m.group('math').replace('*', r' * ') + "$", line)
            line = re.sub(inline_math_pattern, lambda m: "$" + m.group('math').replace('_', r' _ ') + "$", line)

            # Replace backslashes with double backslashes in inline math blocks
            line = re.sub(inline_math_pattern, lambda m: "$" + m.group('math').replace('\\', '\\\\') + "$", line)

            # Check if the line starts a display math block
            if '$$' in line:
                in_display_math_block = True
                # Replace asterisks with "\*" in display math block
                line = re.sub(r'(?<!\\)\*', r'\\*', line)

        # Add the processed line to the new lines list
        new_lines.append(line)

    return new_lines


def all_processor(lines: List[str]) -> List[str]:
    matter, content = parse_front_matter(lines)
    content = process_math_blocks(content)
    lines = add_front_matter(matter, content)
    return lines


def preprocess(src_root: Path, tgt_root: Path, processor: Callable[[List[str]], List[str]]):
    file_cnt = 0
    # create tgt_root if it doesn't exist
    if not tgt_root.exists():
        tgt_root.mkdir(parents=True)
    else:
        clear_folder(tgt_root)

    # recursively traverse the src_root directory
    for src_path in src_root.glob('**/*'):
        # get the relative path of the file or directory from src_root
        rel_path = src_path.relative_to(src_root)

        # create the corresponding tgt_path under tgt_root
        tgt_path = tgt_root / rel_path

        if src_path.is_file():
            print(src_path)
            file_cnt += 1
            # if the file is a Markdown file, process it
            if src_path.suffix == '.md':
                with open(src_path, 'r') as f:
                    lines = f.readlines()
                processed_lines = processor(lines)
                if src_path.name == 'README.md':
                    # if the file is named README.md, copy it to _index.md
                    tgt_path = tgt_path.parent / '_index.md'
                with open(tgt_path, 'w') as f:
                    f.writelines(processed_lines)
            else:
                # if the file is not a Markdown file, simply copy it to tgt_path
                tgt_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(src_path, tgt_path.parent)
        else:
            # if the path is a directory, create the corresponding directory under tgt_root
            tgt_path.mkdir(parents=True, exist_ok=True)
            index_path = tgt_path / "_index.md"
            if not index_path.is_file():
                index_path.touch()
                with open(index_path, "w") as f:
                    f.write("---\nbookCollapseSection: true\nweight: 20\n---\n")

    return file_cnt
