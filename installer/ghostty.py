from pathlib import Path

from installer.base import Installer


class GhosttyInstaller(Installer):
    def install(self) -> bool:
        ok = True
        rel_path = Path(".config") / "ghostty" / "config.ghostty"
        host_path = Path.home() / rel_path.parent / "config"
        dotfile_path = self.dotfiles_home() / rel_path
        ok &= self.make_symlink(dotfile_path, host_path, force=True)
        return ok

    def should_install(self) -> bool:
        return self.is_executable("ghostty")
