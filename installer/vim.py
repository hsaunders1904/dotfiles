from pathlib import Path

from installer.lib import REPO_ROOT, update_dotfile

__all__ = ["install"]

COMMENT_CHAR = '"'
RC_FILE = ".vimrc"
HOME_RC_PATH = Path.home() / RC_FILE
THIS_RC_PATH = REPO_ROOT / "dotfiles" / RC_FILE


def install():
    update_rc_file(THIS_RC_PATH, HOME_RC_PATH)


def update_rc_file(this: Path, dot_file: Path):
    import_str = build_import_str(this)
    update_dotfile(dot_file, import_str, COMMENT_CHAR, new_line="\n")


def build_import_str(file_path: Path) -> str:
    return (
        f'if filereadable("{file_path}")\n'
        f"    exe 'source' \"{file_path}\"\n"
        "endif\n"
    )
