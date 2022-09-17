import os

from installer import _lib as lib
from installer.common import download_z_jump_around

__all__ = ["install"]

EXTERNAL_DIR = os.path.join(lib.REPO_ROOT, "external")
SH_COMMENT_CHAR = "#"
HOME_ZSH_PATH = os.path.join(os.path.expanduser("~"), ".zshrc")
THIS_ZSH_PATH = os.path.join(lib.REPO_ROOT, "dotfiles", ".zshrc")


def install():
    update_zshrc()
    download_z_jump_around(os.path.join(EXTERNAL_DIR, "z.sh"))


def update_zshrc():
    import_str = build_file_import_str(THIS_ZSH_PATH)
    lib.update_dotfile(HOME_ZSH_PATH, import_str, SH_COMMENT_CHAR)


def build_file_import_str(file_path: str):
    return (
        f"if [ -f \"{file_path}\" ]; then\n"
        f"    . \"{file_path}\"\n"
        f"fi"
    )
