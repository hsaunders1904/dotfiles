from installer.base import Installer

GIT_URL = "https://github.com/junegunn/fzf.git"


class FzfInstaller(Installer):
    def install(self) -> bool:
        if not self.update_fzf():
            return False
        return self.install_fzf()

    def update_fzf(self):
        clone_dir = self.fzf_dir()
        if clone_dir.is_dir():
            ok = self.git_pull(clone_dir)
        else:
            ok = self.git_clone(GIT_URL, clone_dir)
        if not ok:
            return False
        return True

    def install_fzf(self):
        fzf_dir = self.fzf_dir()
        install_args = [
            "bash",
            "./install",
            "--no-update-rc",
            "--no-key-bindings",
            "--no-completion",
            "--no-bash",
            "--no-fish",
            "--no-zsh",
        ]
        if not self.run_command(install_args, cwd=str(fzf_dir)):
            return False
        self.local_bin().mkdir(exist_ok=True, parents=True)
        return self.make_symlink(fzf_dir / "bin" / "fzf", self.local_bin() / "fzf")

    def fzf_dir(self):
        return self.external_dir() / "fzf"
