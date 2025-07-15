import os
from pathlib import Path

from installer.base import Installer


class ZshInstaller(Installer):
    OMZ_URL = "https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh"
    COMMENT_CHAR = "#"

    def install(self) -> bool:
        if self.oh_my_zsh_path() is None:
            if not self.install_oh_my_zsh():
                return False
        ok = self.pull_plugins()
        ok |= self.update_zshrc()
        return ok

    def should_install(self) -> bool:
        return self.is_executable("zsh")

    def install_oh_my_zsh(self):
        installer_path = self.external_dir() / "ohmyzsh_install.sh"
        self.download_file(self.OMZ_URL, installer_path, force=True)
        install_cmd = ["sh", installer_path, "--unattended", "--keep-zshrc"]
        return self.run_command(install_cmd)

    def pull_plugins(self) -> bool:
        cmd = ["git", "submodule", "update", "--init", str(self.custom_omz_dir())]
        return self.run_command(cmd)

    def update_zshrc(self) -> bool:
        dotfile = self.repo_root() / "dotfiles" / ".zshrc"
        import_str = "\n".join(
            [
                f'if [ -f "{dotfile}" ]; then',
                f'    . "{dotfile}"',
                "fi",
            ]
        )
        zshrc = Path.home() / ".zshrc"
        return self.update_dotfile(zshrc, import_str, self.COMMENT_CHAR)

    def custom_omz_dir(self):
        return self.repo_root() / "apps" / "oh-my-zsh"

    @staticmethod
    def oh_my_zsh_path() -> Path | None:
        if not (path_str := os.environ.get("ZSH", None)):
            return None
        if (path := Path(path_str)).is_dir():
            return path
        return None
