import argparse
import os
from dataclasses import dataclass

from installer import (
    bash,
    diff_so_fancy,
    font,
    git,
    helix,
    iterm2,
    neovim,
    pixi,
    pwsh,
    vim,
    wsl,
    zed,
    zellij,
    zsh,
)
from installer.base import Installer


@dataclass
class Args:
    pick: list[str]
    skip: list[str]
    dry_run: bool


INSTALLER_CLASSES = [
    pixi.PixiInstaller,
    bash.BashInstaller,
    diff_so_fancy.DiffSoFancyInstaller,
    font.FontInstaller,
    git.GitInstaller,
    helix.HelixInstaller,
    iterm2.Iterm2Installer,
    neovim.NeovimInstaller,
    pwsh.PwshInstaller,
    vim.VimInstaller,
    wsl.WslInstaller,
    zed.ZedInstaller,
    zellij.ZellijInstaller,
    zsh.ZshInstaller,
]


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    dry_run = os.environ.get("DOTFILES_DRY_RUN", str(args.dry_run)) not in [
        "0",
        "False",
    ]
    if install(args.pick, args.skip, dry_run):
        return 0
    return 1


def parse_args(argv: list[str]) -> Args:
    desc = "Install dotfiles.\n\nAvailable installers are:\n"
    desc += "  * " + "\n  * ".join(
        cls.__name__.removesuffix("Installer").lower()
        for cls in Installer.__subclasses__()
    )
    parser = argparse.ArgumentParser(
        "dotfiles",
        description=desc,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--pick",
        nargs="*",
        help="choose which installers to run. You may use this flag more than once",
    )
    parser.add_argument(
        "--skip",
        nargs="*",
        help="choose which installers to skip. You may use this flag more than once",
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        help="show the commands that will be run",
        default=False,
    )
    return Args(**vars(parser.parse_args(argv)))


def install(pick: list[str], skip: list[str], dry_run: bool) -> bool:
    has_error = False
    for installer in [I() for I in INSTALLER_CLASSES]:
        installer.dry_run = dry_run
        name = type(installer).__name__.removesuffix("Installer")
        if (
            (pick and name.lower() not in pick)
            or (skip and name.lower() in skip)
            or (not installer.should_install())
        ):
            print(f"[-] {name}")
            continue
        print(f"[+] {name}")
        if not installer.install():
            installer.logger().warning("%s failed", name)
            has_error = True
    return has_error


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv[1:]))
