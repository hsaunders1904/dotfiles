import os
from pathlib import Path

from lib import EXTERNAL_DIR, download_file

VIM_PLUG_URL = "https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"


def install():
    download_vim_plug()


def download_vim_plug():
    download_file(
        url=VIM_PLUG_URL,
        out_path=Path(EXTERNAL_DIR) / "plug.vim",
        log=True,
        force=True,
    )


# def nvim_data_dir() -> Path | None:
#     if os.name == "nt":
#         if app_data := os.environ.get("LOCALAPPDATA", None):
#             data_dir = Path(app_data) / "nvim-data"
#         else:
#             return None
#     else:
#         data_dir = Path(os.environ.get("XDG_DATA_HOME", "~/.local/share")).expanduser()
#         data_dir = data_dir / "nvim"
#     return data_dir / "site" / "autoload"


if __name__ == "__main__":
    install()
