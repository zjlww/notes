import re
from typing import Callable, List


def math_callback(s: str) -> str:
    # Replace `*` with ` * `
    s = s.replace("*", " * ")
    # Replace `_` with ` _ `
    s = s.replace("_", " _ ")
    # Replace `\` with `\\`
    s = s.replace("\\", "\\\\")
    # Add a space between the square brackets and the parentheses.
    s = re.sub(r"\[(.*?)\]\((.*?)\)", r"[\1] (\2)", s)
    # Return the modified string
    return s    


def process_inline_math(line: str, math_callback: Callable[[str], str]) -> str:
    """
    Given a line from a Markdown file, finds all inline math of form `$xxx$`,
    calls function `math_callback` on `xxx`, and replaces `xxx` with the
    returned value.

    Parameters:
    - line (str): The input line containing inline math expressions.
    - math_callback (Callable[[str], str]): A function that takes a math expression
      as input, and returns a modified math expression as output.

    Returns:
    - str: The input line with all inline math expressions replaced by the output
      of `math_callback`.

    Example:
    >>> def math_callback(math):
    ...     return f"Math expression: {math}"
    ...
    >>> line = "The value of $x$ is $2x+3$."
    >>> processed_line = process_inline_math(line, math_callback)
    >>> print(processed_line)
    The value of Math expression: x is Math expression: 2x+3.
    """
    regex = r"\$([^$]+?)\$"
    inline_math = re.findall(regex, line)
    for math in inline_math:
        replacement = math_callback(math)
        line = line.replace(f"${math}$", f"${replacement}$")
    return line


def process_block_math(lines: List[str], math_callback: Callable[[str], str]) -> List[str]:
    # Initialize an empty list to store the modified lines
    result = []
    # Initialize a boolean variable to indicate whether we are inside a math block
    is_in_block_math = False
    # Loop over each line in the input `lines` list
    for line in lines:
        if is_in_block_math:
            # If we are inside a math block, check if the current line is the end of the block
            if line.strip() == "$$":
                # If it is, set `is_in_block_math` to `False`
                is_in_block_math = False
            # Append the current line to the `result` list, after calling `math_callback` on the line
            result.append(math_callback(line))
        else:
            # If we are not inside a math block, check if the current line is the start of a math block
            if line.strip().startswith("$$"):
                # If it is, set `is_in_block_math` to `True`, and append the current line to the `result` list
                is_in_block_math = True
            result.append(line)
    # Return the `result` list, which contains all the modified lines of the input Markdown file
    return result


def math_processor(lines: List[str]) -> List[str]:
    lines = process_block_math(lines, math_callback)
    lines = [process_inline_math(line, math_callback) for line in lines]
    return lines
