from pathlib import Path

from installer.base import Installer


class VimInstaller(Installer):
    COMMENT_CHAR = '"'

    def install(self) -> bool:
        vimrc = Path.home() / ".vimrc"
        dotfile = self.repo_root() / "dotfiles" / ".vimrc"
        import_str = "\n".join(
            [
                f'if filereadable("{dotfile}")',
                f"    exe 'source' \"{dotfile}\"",
                "endif",
                "",
            ]
        )
        return self.update_dotfile(vimrc, import_str, self.COMMENT_CHAR)

    def should_install(self) -> bool:
        return self.is_executable("vim")
