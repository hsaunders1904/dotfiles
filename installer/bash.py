import os

from installer import lib

__all__ = ["install"]

SH_COMMENT_CHAR = "#"
HOME_BASHRC_PATH = os.path.expanduser("~/.bashrc")
THIS_BASHRC_PATH = os.path.join(lib.REPO_ROOT, "dotfiles", ".bashrc")


def install():
    update_bashrc()


def update_bashrc():
    import_str = build_file_import_str(THIS_BASHRC_PATH)
    lib.update_dotfile(HOME_BASHRC_PATH, import_str, SH_COMMENT_CHAR, new_line="\n")


def build_file_import_str(file_path: str):
    return f'if [ -f "{file_path}" ]; then\n    . "{file_path}"\nfi'
