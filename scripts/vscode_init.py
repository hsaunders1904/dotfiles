#!/usr/bin/env python3

"""
Initialise a .vscode directory within the working directory, and create
the usual files if they don't exist.
"""

import argparse
from pathlib import Path

LAUNCH_TEMPLATE = """{
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": []
}"""
TASKS_TEMPLATE = """{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": []
}"""


def parse_args() -> Path:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    default_path = Path.cwd()
    parser.add_argument(
        "path",
        type=Path,
        help=(
            "the directory to create the '.vscode/' directory within "
            f"[default: {default_path}]"
        ),
        default=default_path,
        nargs="?",
    )
    args = parser.parse_args()
    return args.path


def write_file_if_not_exists(path: Path, content: str):
    if not path.is_file():
        path.write_text(content)
        print(f"Created {path}")


def main():
    target_dir = parse_args()
    vscode_dir = target_dir / ".vscode"
    vscode_dir.mkdir(exist_ok=True)
    write_file_if_not_exists(vscode_dir / "settings.json", "{}")
    write_file_if_not_exists(vscode_dir / ".gitignore", "*\n")
    write_file_if_not_exists(vscode_dir / "launch.json", LAUNCH_TEMPLATE)
    write_file_if_not_exists(vscode_dir / "tasks.json", TASKS_TEMPLATE)


if __name__ == "__main__":
    main()
