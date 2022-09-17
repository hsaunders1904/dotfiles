import shutil

from installer import bash, vim, zsh, git


def is_executable(exe_name: str) -> bool:
    return bool(shutil.which(exe_name))


def install():
    if is_executable("bash"):
        bash.install()
    if is_executable("zsh"):
        zsh.install()
    if is_executable("git"):
        git.install()
    if is_executable("vim"):
        vim.install()


if __name__ == "__main__":
    install()
