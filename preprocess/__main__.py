from . import *
import shutil

print("Preprocessing ... ", end="")
cnt = preprocess(
    normalize_path("./notes/"),
    normalize_path("./content/docs/"),
    all_processor
)
print(f"{cnt} files processed.")

shutil.copy(
    normalize_path("./README.md"),
    normalize_path("content/_index.md")
)
