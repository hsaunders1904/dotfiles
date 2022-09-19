import os
import shutil

from installer import bash, git, pwsh, vim, zsh
from installer.lib import REPO_ROOT
from installer.common import download_z_jump_around
from installer.lib import REPO_ROOT

EXTERNAL_DIR = os.path.join(REPO_ROOT, "external")


def is_executable(exe_name: str) -> bool:
    return bool(shutil.which(exe_name))


def install():
    if is_executable("bash"):
        bash.install()
    if is_executable("zsh"):
        zsh.install()
    if is_executable("bash") or is_executable("zsh"):
        out_path = os.path.join(EXTERNAL_DIR, "z.sh")
        if not os.path.isfile(out_path):
            download_z_jump_around(out_path)
    if is_executable("git"):
        git.install()
    if is_executable("vim"):
        vim.install()
    if is_executable("pwsh"):
        pwsh.install()


if __name__ == "__main__":
    install()
