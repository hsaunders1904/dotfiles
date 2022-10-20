import shutil

from installer import bash, diff_so_fancy, git, pwsh, vim, wsl, z, zsh


def is_executable(exe_name: str) -> bool:
    return bool(shutil.which(exe_name))


def install():
    if is_executable("bash"):
        bash.install()
        if wsl.is_wsl():
            wsl.install()
    if is_executable("zsh"):
        zsh.install()
    if is_executable("bash") or is_executable("zsh"):
        z.install()
    if is_executable("git"):
        git.install()
        diff_so_fancy.install()
    if is_executable("vim"):
        vim.install()
    if is_executable("pwsh"):
        pwsh.install()


if __name__ == "__main__":
    install()
