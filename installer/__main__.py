import os

from installer import bash, diff_so_fancy, font, fzf, git, neovim, pwsh, vim, wsl, zsh
from installer.base import Installer


def install():
    installers: list[Installer] = [
        bash.BashInstaller(),
        zsh.ZshInstaller(),
        git.GitInstaller(),
        diff_so_fancy.DiffSoFancyInstaller(),
        vim.VimInstaller(),
        neovim.NeovimInstaller(),
        pwsh.PwshInstaller(),
        font.FontInstaller(),
        wsl.WslInstaller(),
        fzf.FzfInstaller(),
    ]

    dry_run = os.environ.get("DOTFILES_DRY_RUN") not in ["0", None]
    for installer in installers:
        name = type(installer).__name__.removesuffix("Installer")
        installer.dry_run = dry_run
        if not installer.should_install():
            print(f"[-] {name}")
            continue
        print(f"[+] {name}")
        if not installer.install():
            installer.logger().warning("%s failed", name)


if __name__ == "__main__":
    install()
