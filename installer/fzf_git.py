from installer.base import Installer


class FzfGitInstaller(Installer):
    GIT_URL = "https://github.com/junegunn/fzf-git.sh.git"

    def install(self) -> bool:
        clone_dir = self.external_dir() / "fzf-git"
        if clone_dir.is_dir():
            return self.git_pull(clone_dir)
        return self.git_clone(self.GIT_URL, clone_dir)

    def should_install(self) -> bool:
        return self.is_executable("git") and self.is_executable("fzf")
