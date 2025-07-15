import os
import shutil
from pathlib import Path

from installer.base import Installer


class BashInstaller(Installer):
    COMMENT_CHAR = "#"

    def install(self) -> bool:
        bashrc = Path.home() / ".bashrc"
        dotfiles_bashrc = self.repo_root() / "dotfiles" / ".bashrc"
        import_str = _build_file_import_str(dotfiles_bashrc)
        self.update_dotfile(bashrc, import_str, self.COMMENT_CHAR)
        return True

    def should_install(self) -> bool:
        return self.is_executable("bash")


def _build_file_import_str(file_path: Path):
    return f'if [ -f "{file_path}" ]; then\n    . "{file_path}"\nfi'
