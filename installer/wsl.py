import os
import stat
from pathlib import Path

from installer import lib

PWSH_EXE_LINE = (
    "PowershellExe="
    r"${PowershellExe:-/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe}"
)
PWSH_EXE_NO_PROFILE = (
    "PowershellExe="
    r'"${PowershellExe:-/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe} '
    '-NoProfile"'
)
PROC_VERSION = "/proc/version"
WSL_OPEN = "wsl-open"
WSL_OPEN_URL = "https://raw.githubusercontent.com/4U6U57/wsl-open/master/wsl-open.sh"
XDG_OPEN = "xdg-open"


def install():
    install_wsl_open()


def is_wsl() -> bool:
    try:
        return "microsoft" in Path(PROC_VERSION).read_text().lower()
    except Exception:
        return False


def install_wsl_open():
    local_bin = _make_local_bin_dir()
    out_path = os.path.join(local_bin, WSL_OPEN)
    lib.download_file(WSL_OPEN_URL, out_path, force=True)
    if os.path.isfile(out_path):
        _make_executable(out_path)
        _make_symlink_if_not_exist(out_path, os.path.join(local_bin, XDG_OPEN))
        _append_no_profile_to_pwsh(out_path)


def _make_local_bin_dir() -> str:
    local_bin = os.path.expanduser("~/.local/bin")
    os.makedirs(local_bin, exist_ok=True)
    return local_bin


def _make_executable(file_path: str):
    st = os.stat(file_path)
    os.chmod(file_path, st.st_mode | stat.S_IEXEC)


def _make_symlink_if_not_exist(origin: str, link: str):
    if not os.path.isfile(link):
        lib.run_command(["ln", "-s", origin, link])


def _append_no_profile_to_pwsh(file_path: str):
    """
    Replace the pwsh exe in the file content so it runs with -NoProfile.

    This is a bit of a hack to avoid powershell error: 'running scripts
    is disabled on this system'.
    """
    text = Path(file_path).read_text()
    with open(file_path, "w") as f:
        f.write(_replace_pwsh_exe_str(text))


def _replace_pwsh_exe_str(file_content: str) -> str:
    lines = []
    for line in file_content.split("\n"):
        if line.rstrip() == PWSH_EXE_LINE:
            lines.append(PWSH_EXE_NO_PROFILE)
        else:
            lines.append(line)
    return "\n".join(lines)
