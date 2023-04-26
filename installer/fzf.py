import os
import subprocess

from installer import lib

__all__ = ["install"]

GIT_URL = "https://github.com/junegunn/fzf.git"


def install():
    clone_dir = os.path.join(lib.EXTERNAL_DIR, "fzf")
    if os.path.exists(clone_dir):
        _git_pull(clone_dir)
    else:
        _git_clone(GIT_URL, clone_dir)
    lib.run_command(
        [
            "bash",
            "./install",
            "--no-update-rc",
            "--no-key-bindings",
            "--no-completion",
            "--no-bash",
            "--no-fish",
            "--no-zsh",
        ],
        cwd=clone_dir,
    )
    local_bin = lib.make_local_bin_dir()
    lib.make_symlink_if_not_exist(
        os.path.join(clone_dir, "bin", "fzf"),
        os.path.join(local_bin, "fzf"),
    )


def _git_clone(url: str, clone_dir: str):
    print(f"[+] Cloning '{url}'")
    subprocess.run(["git", "clone", url, clone_dir])


def _git_pull(repo_dir: str):
    print(f"[+] Pulling '{repo_dir}'")
    subprocess.run(["git", "-C", repo_dir, "pull"])
