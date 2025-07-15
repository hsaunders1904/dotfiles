import os
import platform
import shutil

from installer import bash, diff_so_fancy, font, fzf, git, neovim, pwsh, vim, wsl, zsh
from installer.base import Installer


def is_executable(exe_name: str) -> bool:
    return bool(shutil.which(exe_name))


def install():
    installers: list[Installer] = [
        bash.BashInstaller(),
        zsh.ZshInstaller(),
        git.GitInstaller(),
        diff_so_fancy.DiffSoFancyInstaller(),
        vim.VimInstaller(),
    ]

    dry_run = os.environ.get("DOTFILES_DRY_RUN") not in ["0", None]
    for installer in installers:
        name = type(installer).__name__
        print(f"[+] {name}")
        installer.dry_run = dry_run
        if installer.should_install():
            if not installer.install():
                installer.logger().warning("%s failed", name)

    # if is_executable("vim"):
    #     print("Vim...")
    #     vim.install()
    # if is_executable("nvim"):
    #     print("Neovim...")
    #     neovim.install()
    # if is_executable("pwsh"):
    #     print("PowerShell...")
    #     pwsh.install()
    # if platform.system() != "Windows":
    #     print("Fonts...")
    #     font.install()
    # if platform.system() == "Linux":
    #     if wsl.is_wsl():
    #         print("WSL...")
    #         wsl.install()
    #     # The apt package for fzf on Debian is really old, so lacks a
    #     # lot of features. Install manually here instead.
    #     print("fzf...")
    #     fzf.install()


if __name__ == "__main__":
    install()
