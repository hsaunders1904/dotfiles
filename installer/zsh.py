import os

from installer import _lib as lib

__all__ = ["install"]

SH_COMMENT_CHAR = "#"
HOME_ZSH_PATH = os.path.join(os.path.expanduser("~"), ".zshrc")
THIS_ZSH_PATH = os.path.join(lib.REPO_ROOT, "dotfiles", ".zshrc")


def install():
    update_zshrc()


def update_zshrc():
    import_str = build_file_import_str(THIS_ZSH_PATH)
    lib.update_dotfile(HOME_ZSH_PATH, import_str, SH_COMMENT_CHAR)


def build_file_import_str(file_path: str):
    return (
        f"if [ -f \"{file_path}\" ]; then\n"
        f"    . \"{file_path}\"\n"
        f"fi"
    )
