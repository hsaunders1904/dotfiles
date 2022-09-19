import os

from installer.lib import REPO_ROOT, update_dotfile

COMMENT_CHAR = '"'
RC_FILE = ".vimrc"
HOME_RC_PATH = os.path.join(os.path.expanduser("~"), RC_FILE)
THIS_RC_PATH = os.path.join(REPO_ROOT, "dotfiles", RC_FILE)


def install():
    update_rc_file()


def update_rc_file():
    import_str = build_import_str(THIS_RC_PATH)
    update_dotfile(HOME_RC_PATH, import_str, COMMENT_CHAR, new_line="\n")


def build_import_str(file_path: str) -> str:
    return (
        f'if filereadable("{file_path}")\n'
        f"    exe 'source' \"{file_path}\"\n"
        "endif\n"
    )
