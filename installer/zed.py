from pathlib import Path

from installer.base import Installer


class ZedInstaller(Installer):
    def install(self) -> bool:
        ok = True
        for config_file in ["keymap.json", "settings.json"]:
            rel_path = Path(".config") / "zed" / config_file
            host_path = Path.home() / rel_path
            dotfile_path = self.dotfiles_home() / rel_path
            ok &= self.make_symlink(dotfile_path, host_path, force=True)
        return ok

    def should_install(self) -> bool:
        return self.is_executable("zed")
