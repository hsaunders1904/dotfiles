import os
import re
import subprocess
from pathlib import Path
from typing import List
from urllib import request

DRY_RUN = False
REPO_ROOT = Path(__file__).parent.parent
REGION_START = ">>> hsaunders1904/dotfiles >>>"
REGION_END = "<<< hsaunders1904/dotfiles <<<"


def run_command_get_output(args: List[str]) -> str:
    result = subprocess.run(args, stdout=subprocess.PIPE)
    return result.stdout.decode()


def run_command(args: List[str]):
    print(f"[+] {' '.join(args)}")
    if DRY_RUN:
        return
    subprocess.run(args, check=True)


def update_dotfile(file_path: str, new_region_content: str, comment_char: str):
    print(f"[+] Updating file '{file_path}'")
    if DRY_RUN:
        return
    file_content = read_file_if_exists(file_path)
    new_content = update_dotfile_region(file_content, new_region_content, comment_char)
    with open(file_path, "w") as f_writer:
        f_writer.write(new_content)


def update_dotfile_region(string: str, new_content: str, comment_char: str):
    region_re = (
        f"{comment_char} *{REGION_START}\n"
        r"([\s\S]*)\n"
        f"{comment_char} *{REGION_END}\n"
    )
    re_pattern = re.compile(region_re, re.MULTILINE)
    match = re_pattern.search(string)

    if new_content.endswith("\n"):
        new_content = new_content[:-1]
    new_region = (
        f"{comment_char} {REGION_START}\n"
        f"{new_content}\n"
        f"{comment_char} {REGION_END}\n"
    )
    if match:
        return re_pattern.sub(new_region, string)
    else:
        if string == "":
            return new_region
        else:
            return f"{string}\n{new_region}"


def download_file(url: str, out_path: str, log=True, force: bool = False):
    if log:
        print(f"[+] Downloading '{url}' -> '{out_path}'")
    if os.path.isfile(out_path) and not force:
        return
    if DRY_RUN:
        return
    try:
        _download(url, out_path)
    except Exception as exc:
        print(f"download failed: {exc}")


def _download(url: str, out_path: str):
    request.urlretrieve(url, out_path)


def read_file_if_exists(file_path: str) -> str:
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""
    except OSError as os_error:
        print(f"could not read file '{file_path}': {os_error}.")
