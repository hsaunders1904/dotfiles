import os
import subprocess

from installer import lib

__all__ = ["install"]

GIT_URL = "https://github.com/so-fancy/diff-so-fancy.git"


def install():
    clone_dir = os.path.join(lib.EXTERNAL_DIR, "diff-so-fancy")
    if os.path.exists(clone_dir):
        _git_pull(clone_dir)
    else:
        _git_clone(GIT_URL, clone_dir)


def _git_clone(url: str, clone_dir: str):
    print(f"[+] Cloning '{url}'")
    subprocess.run(["git", "clone", url, clone_dir])


def _git_pull(repo_dir: str):
    print(f"[+] Pulling '{repo_dir}'")
    subprocess.run(["git", "-C", repo_dir, "pull"])
