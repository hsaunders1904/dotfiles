import os
import stat
from pathlib import Path

from installer import lib

PROC_VERSION = "/proc/version"
WSL_OPEN = "wsl-open"
WSL_OPEN_URL = "https://gitlab.com/4U6U57/wsl-open/-/raw/master/wsl-open.sh"
XDG_OPEN = "xdg-open"


def install():
    install_wsl_open()


def is_wsl() -> bool:
    try:
        return "microsoft" in Path(PROC_VERSION).read_text().lower()
    except Exception:
        return False


def install_wsl_open():
    out_path = os.path.join(lib.EXTERNAL_DIR, WSL_OPEN)
    lib.download_file(WSL_OPEN_URL, out_path, force=True)
    if not os.path.isfile(out_path):
        return
    _make_executable(out_path)
    local_bin = lib.make_local_bin_dir()
    lib.make_symlink_if_not_exist(out_path, os.path.join(local_bin, WSL_OPEN))
    lib.make_symlink_if_not_exist(out_path, os.path.join(local_bin, XDG_OPEN))


def _make_executable(file_path: str):
    st = os.stat(file_path)
    os.chmod(file_path, st.st_mode | stat.S_IEXEC)
