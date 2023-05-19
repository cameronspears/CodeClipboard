import os
import pyperclip
from io import StringIO
from settings import project_path

def create_tree_dict(all_files, project_path):
    tree_dict = {os.path.basename(project_path): {}}
    for file_path in all_files:
        relative_path = file_path.replace(project_path + os.sep, '')
        parts = relative_path.split(os.sep)
        cur_dict = tree_dict[os.path.basename(project_path)]
        for part in parts[:-1]:
            if part not in cur_dict:
                cur_dict[part] = {}
            cur_dict = cur_dict[part]
        cur_dict[parts[-1]] = None
    return tree_dict

def display_tree_from_dict(tree_dict, prefix="", output_stringio=None):
    keys = sorted(tree_dict.keys())
    for key in keys:
        value = tree_dict[key]
        if isinstance(value, dict):
            print(prefix + ('└─ ' if key == keys[-1] else '├─ ') + key + '/', file=output_stringio)
            display_tree_from_dict(value, prefix + ('   ' if key == keys[-1] else '│  '), output_stringio)
        else:
            print(prefix + ('└─ ' if key == keys[-1] else '├─ ') + key, file=output_stringio)

def copy_project_to_clipboard(project_path):
    all_files = []
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                all_files.append(file_path)

    tree_dict = create_tree_dict(all_files, project_path)

    # Display ASCII tree structure
    output_stringio = StringIO()
    print("Project structure:", file=output_stringio)
    display_tree_from_dict(tree_dict, output_stringio=output_stringio)
    ascii_tree = output_stringio.getvalue()
    print(ascii_tree)

    for i, file in enumerate(all_files):
        display_file = file.replace(project_path + os.sep, '')
        print(f"{i}: {display_file}")

    selected_files = input("Enter the numbers of the files you want to select, separated by commas: ")
    selected_files = selected_files.split(',')  # split input into list by comma
    selected_files = [all_files[int(i.strip())] for i in selected_files]  # convert numbers to files

    clipboard_content = ascii_tree + "####################################################\n"
    for file_path in selected_files:
        clipboard_content += f"File: {file_path}\n"

        try:
            with open(file_path, "r", encoding='utf-8') as f:
                file_content = "\n".join(line.strip() for line in f.readlines())
        except UnicodeDecodeError:
            file_content = "<Could not decode file>"
                
        clipboard_content += f"Content:\n{file_content}\n\n"

    pyperclip.copy(clipboard_content)
    print("Successfully copied to clipboard!")

copy_project_to_clipboard(project_path)