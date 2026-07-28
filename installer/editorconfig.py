from pathlib import Path

from installer.base import Installer


class EditorConfigInstaller(Installer):
    def install(self) -> bool:
        dotfile = self.dotfiles_home() / ".editorconfig"
        return self.make_symlink(dotfile, Path.home() / ".editorconfig")

    def should_install(self) -> bool:
        return self.is_executable("zed")
