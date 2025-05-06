import platform
import shutil

from installer import bash, diff_so_fancy, font, fzf, git, neovim, pwsh, vim, wsl, zsh


def is_executable(exe_name: str) -> bool:
    return bool(shutil.which(exe_name))


def install():
    if is_executable("bash"):
        print("Bash...")
        bash.install()
    if is_executable("zsh"):
        print("Zsh...")
        zsh.install()
    if is_executable("git"):
        print("Git...")
        git.install()
        print("diff-so-fancy...")
        diff_so_fancy.install()
    if is_executable("vim"):
        print("Vim...")
        vim.install()
    if is_executable("nvim"):
        print("Neovim...")
        neovim.install()
    if is_executable("pwsh"):
        print("PowerShell...")
        pwsh.install()
    if platform.system() != "Windows":
        print("Fonts...")
        font.install()
    if platform.system() == "Linux":
        if wsl.is_wsl():
            print("WSL...")
            wsl.install()
        # The apt package for fzf on Debian is really old, so lacks a
        # lot of features. Install manually here instead.
        print("fzf...")
        fzf.install()


if __name__ == "__main__":
    install()
