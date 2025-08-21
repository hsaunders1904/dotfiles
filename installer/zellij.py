from pathlib import Path

from installer.base import Installer


class ZellijInstaller(Installer):
    def install(self) -> bool:
        rel_config = Path(".config") / "zellij" / "config.kdl"
        host_config = Path.home() / rel_config
        dotfiles_config = self.dotfiles_home() / rel_config
        return self.make_symlink(dotfiles_config, host_config, force=True)

    def should_install(self) -> bool:
        return self.is_executable("zellij")
