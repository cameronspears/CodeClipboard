# CodeClipboard

The CodeClipboard is a Python utility tool that helps you quickly get a snapshot of your project structure and select files, copying them to your clipboard in a nicely formatted way. This can be particularly helpful when you need to quickly share your project structure and file contents with others.

## Getting Started

To get started with CodeClipboard, you need to have Python installed on your system. The CodeClipboard has been tested with Python 3.8 and later versions.

### Prerequisites

CodeClipboard relies on the `pyperclip` package for interacting with the clipboard. If you don't have `pyperclip` installed, you can install it using pip:

```
bashCopy code
pip install pyperclip
```

### Installing

To use CodeClipboard, first clone the repository to your local machine:

```
bashCopy code
git clone https://github.com/<your_username>/CodeClipboard.git
```

Then, navigate to the directory where the repository is cloned:

```
bashCopy code
cd CodeClipboard
```

## Usage

First, you need to set the `project_path` variable in `settings.py` to point to the root directory of the project you want to analyze:

```
pythonCopy code
project_path = r"/path/to/your/project" # Change this to your project path
```

Then, simply run the `CodeClipboard.py` script:

```
bashCopy code
python CodeClipboard.py
```

This will print an ASCII tree representing the project structure to stdout and prompt you to select the numbers of the files you want to copy to your clipboard. Enter the numbers of the files, separated by commas, and hit Enter.

The selected file contents, along with the project structure, will be copied to your clipboard, ready to be pasted wherever you need.