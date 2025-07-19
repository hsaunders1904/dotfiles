import os
import stat
from pathlib import Path

from installer.base import Installer


class WslInstaller(Installer):
    PROC_VERSION = "/proc/version"
    WSL_OPEN_URL = "https://gitlab.com/4U6U57/wsl-open/-/raw/master/wsl-open.sh"

    def install(self) -> bool:
        return self.install_wsl_open()

    def should_install(self) -> bool:
        return self.os_is_wsl()

    def install_wsl_open(self) -> bool:
        out_path = self.external_dir() / "wsl-open"
        if not self.download_file(self.WSL_OPEN_URL, out_path, force=True):
            return False
        if not out_path.is_file():
            return False
        _make_executable(out_path)
        symlink_path = Path.home() / ".local" / "bin"
        symlink_path.mkdir(exist_ok=True, parents=True)
        ok = self.make_symlink(out_path, symlink_path / "wsl-open")
        ok &= self.make_symlink(out_path, symlink_path / "xdg-open")
        return ok

    def os_is_wsl(self) -> bool:
        try:
            return "microsoft" in Path(self.PROC_VERSION).read_text().lower()
        except Exception:
            return False


def _make_executable(file_path: Path):
    st = file_path.stat()
    file_path.chmod(st.st_mode | stat.S_IEXEC)
