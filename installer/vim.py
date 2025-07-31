from pathlib import Path

from installer.base import Installer


class VimInstaller(Installer):
    COMMENT_CHAR = '"'

    def install(self) -> bool:
        vimrc = Path.home() / ".vimrc"
        dotfile = self.dotfiles_home() / ".vimrc"
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
        if not self.is_executable("vim"):
            self.logger().debug("skipping: 'vim' not found")
            return False
        return True
