import os
import sys
from pathlib import Path

from installer.base import Installer


class HelixInstaller(Installer):
    def install(self) -> bool:
        local_dir = self.dotfiles_home() / ".config" / "helix"
        if (conf_dir := self.config_dir()) is None:
            return False
        conf_dir.mkdir(exist_ok=True)
        ok = True
        for file in ["config.toml", "languages.toml"]:
            content = (local_dir / file).read_text().rstrip("\n")
            host_file = conf_dir / file
            ok &= self.update_dotfile(host_file, content, "#")
        return ok

    def should_install(self) -> bool:
        return self.is_executable("hx")

    def config_dir(self) -> Path | None:
        if sys.platform.startswith("win"):
            if app_data := os.environ.get("APPDATA"):
                return Path(app_data) / "helix"
            return None
        return Path.home() / ".config" / "helix"
