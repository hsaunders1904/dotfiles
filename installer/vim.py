import os
from pathlib import Path

from installer.lib import (
    EXTERNAL_DIR,
    REPO_ROOT,
    download_file,
    run_command,
    update_dotfile,
)

__all__ = ["install_vim", "install_neovim"]

COMMENT_CHAR = '"'
RC_FILE = ".vimrc"
HOME_RC_PATH = Path.home() / RC_FILE
THIS_RC_PATH = REPO_ROOT / "dotfiles" / RC_FILE
VIM_PLUG_URL = "https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"


def install_vim():
    update_rc_file(THIS_RC_PATH, HOME_RC_PATH)


def install_neovim():
    download_vim_plug()
    dotfile = REPO_ROOT / "dotfiles" / "init.vim"
    config_path = nvim_init_path()
    config_path.parent.mkdir(parents=True, exist_ok=True)
    update_rc_file(dotfile, config_path)
    run_command(
        [
            "nvim",
            "--clean",
            "-S",
            f"{dotfile}",
            "-c",
            "PlugInstall",
            "-Es",
        ],
        shell=False,
        check=False,
    )


def download_vim_plug() -> Path:
    out = Path(EXTERNAL_DIR) / "plug.vim"
    download_file(
        url=VIM_PLUG_URL,
        out_path=Path(EXTERNAL_DIR) / "plug.vim",
        log=True,
        force=True,
    )
    return out


def update_rc_file(this: Path, dot_file: Path):
    import_str = build_import_str(this)
    update_dotfile(dot_file, import_str, COMMENT_CHAR, new_line="\n")


def build_import_str(file_path: Path) -> str:
    return (
        f'if filereadable("{file_path}")\n'
        f"    exe 'source' \"{file_path}\"\n"
        "endif\n"
    )


def nvim_init_path() -> Path:
    if os.name == "nt":
        app_data = os.environ.get("LOCALAPPDATA", "~/AppData/Local")
        return Path(app_data).expanduser() / "nvim" / "init.vim"
    xdg_config = Path(os.environ.get("XDG_CONFIG_HOME", "~/.config"))
    return (xdg_config / "nvim" / "init.vim").expanduser()
