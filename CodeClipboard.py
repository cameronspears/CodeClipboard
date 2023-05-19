# CodeClipboard.py

import os
import pyperclip
from pathlib import Path
from io import StringIO
from settings import project_path


def create_tree_dict(project_path):
    tree_dict = {os.path.basename(project_path): {}}
    all_files = list(Path(project_path).rglob('*.py'))  # retrieves all Python files

    for file_path in all_files:
        relative_path = file_path.relative_to(project_path).parts
        cur_dict = tree_dict[os.path.basename(project_path)]
        for part in relative_path[:-1]:
            cur_dict = cur_dict.setdefault(part, {})
        cur_dict[relative_path[-1]] = None
    return tree_dict, all_files


def display_tree_from_dict(tree_dict, prefix="", output_stringio=None):
    keys = sorted(tree_dict.keys())
    for key in keys:
        value = tree_dict[key]
        end_line = '└─ ' if key == keys[-1] else '├─ '
        if isinstance(value, dict):
            print(f"{prefix}{end_line}{key}/", file=output_stringio)
            display_tree_from_dict(value, prefix + ('   ' if key == keys[-1] else '│  '), output_stringio)
        else:
            print(f"{prefix}{end_line}{key}", file=output_stringio)


def copy_project_to_clipboard(project_path):
    tree_dict, all_files = create_tree_dict(project_path)

    # Capture ASCII tree structure
    output_stringio = StringIO()
    print("Project structure:", file=output_stringio)
    display_tree_from_dict(tree_dict, output_stringio=output_stringio)
    ascii_tree = output_stringio.getvalue()

    print(ascii_tree)  # This will print the ASCII tree to stdout

    for i, file in enumerate(all_files):
        display_file = str(file.relative_to(project_path))
        print(f"{i}: {display_file}")

    selected_files = input("Enter the numbers of the files you want to select, separated by commas: ")
    selected_files = [all_files[int(i.strip())] for i in selected_files.split(',')]  # convert numbers to files

    clipboard_content = ascii_tree + "####################################################\n"
    for file_path in selected_files:
        try:
            with open(file_path, "r", encoding='utf-8') as f:
                file_content = "\n".join(line.strip() for line in f)
        except UnicodeDecodeError:
            file_content = "<Could not decode file>"

        clipboard_content += f"File: {file_path}\nContent:\n{file_content}\n\n"

    pyperclip.copy(clipboard_content)
    print("Successfully copied to clipboard!")


if __name__ == "__main__":
    copy_project_to_clipboard(project_path)
