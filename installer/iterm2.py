from pathlib import Path

from installer.base import Installer


class Iterm2Installer(Installer):
    def install(self) -> bool:
        rel_path = self.profiles_file()
        return self.make_symlink(self.dotfiles_home() / rel_path, Path.home() / rel_path)

    def should_install(self) -> bool:
        return (Path.home() / self.profiles_file().parent).is_dir()

    def profiles_file(self) -> Path:
        return Path(".config/iterm2/AppSupport/DynamicProfiles/Profiles.json")
