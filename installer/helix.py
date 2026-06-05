import os
import sys
from pathlib import Path

from installer.base import Installer


class HelixInstaller(Installer):
    def install(self) -> bool:
        local_dir = self.dotfiles_home() / ".config" / "helix"
        if (conf_dir := self.config_dir()) is None:
            return False
        conf_dir.mkdir(parents=True, exist_ok=True)
        ok = True
        for file in ["config.toml", "languages.toml"]:
            content = (local_dir / file).read_text().rstrip("\n")
            host_file = conf_dir / file
            ok &= self.update_dotfile(host_file, content, "#")

        # Themes
        themes_dir = self.config_dir() / "themes"
        themes_dir.mkdir(exist_ok=True)
        for theme_file in (local_dir / "themes").glob("*.toml"):
            ok &= self.make_symlink(theme_file, themes_dir / theme_file.name, force=True)
        return ok

    def should_install(self) -> bool:
        return self.is_executable("hx")

    def config_dir(self) -> Path:
        if sys.platform.startswith("win"):
            app_data = os.environ.get("APPDATA", str(Path.home()/"AppData"/"Roaming"))
            return Path(app_data) / "helix"
        return Path.home() / ".config" / "helix"
