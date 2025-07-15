from installer.base import Installer


class DiffSoFancyInstaller(Installer):
    GIT_URL = "https://github.com/so-fancy/diff-so-fancy.git"

    def install(self) -> bool:
        clone_dir = self.external_dir() / "diff-so-fancy"
        if clone_dir.is_dir():
            return self.git_pull(clone_dir)
        return self.git_clone(self.GIT_URL, clone_dir)

    def should_install(self) -> bool:
        return self.is_executable("git")
