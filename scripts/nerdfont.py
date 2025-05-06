#!/usr/bin/env python3
"""
Download and install Nerd Fonts on Windows, Linux or MacOS.

https://www.nerdfonts.com/
"""

import argparse
import enum
import logging
import sys
import tarfile
from dataclasses import dataclass
from pathlib import Path
from urllib import request

BASE_DOWNLOAD_URL = "https://github.com/ryanoasis/nerd-fonts/releases/latest/download"
LINUX_FONT_INSTALL_DIR = Path("~/.local/share/fonts").expanduser()
MACOS_FONT_INSTALL_DIR = Path("~/Library/Fonts").expanduser()

logging.basicConfig(format="%(name)s: %(levelname)s: %(message)s")
logger = logging.getLogger("nerdfont")


@dataclass
class CliArgs:
    fonts: list[str]


class Os(enum.Enum):
    LINUX = enum.auto()
    MACOS = enum.auto()


def main(argv: list[str]) -> int:
    """Download and install nerd fonts."""
    args = parse_args(argv)
    try:
        operating_system = get_os()
    except ValueError:
        logging.exception("could not get fonts directory:")
        return 1
    for font in args.fonts:
        url = f"{BASE_DOWNLOAD_URL}/{font}.tar.xz"
        if out_dir := get_fonts_dir(font, operating_system):
            download_and_extract_tar(url, out_dir)
    return 0


def parse_args(argv: list[str]) -> CliArgs:
    parser = argparse.ArgumentParser(
        "nerdfont",
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("fonts", nargs="+", help="the names of the fonts to install")
    return CliArgs(**vars(parser.parse_args(argv)))


def get_fonts_dir(font_name: str, operating_system: Os) -> Path | None:
    """
    Get the directory in which to install fonts.

    Return ``None`` if the directory to install fonts into is not known.
    """
    if operating_system == Os.LINUX:
        return LINUX_FONT_INSTALL_DIR / font_name
    if operating_system == Os.MACOS:
        return MACOS_FONT_INSTALL_DIR / font_name
    return None


def get_os() -> Os:
    if sys.platform.startswith("linux"):
        return Os.LINUX
    if sys.platform.startswith("darwin"):
        return Os.MACOS
    raise ValueError(f"unsupported platform '{sys.platform}'")


def download_and_extract_tar(url: str, out_dir: Path):
    """Download and extract a nerd font into the given directory."""
    try:
        with (
            request.urlopen(url) as response,
            tarfile.open(fileobj=response, mode="r|xz") as tar,
        ):
            tar.extractall(out_dir, filter=_tar_filter)
    except Exception:
        logger.exception("failed to install '%s'", url)


def _tar_filter(member: tarfile.TarInfo, path: str, /) -> tarfile.TarInfo | None:
    member = tarfile.tar_filter(member, dest_path=path)
    member = tarfile.data_filter(member, dest_path=path)
    if Path(member.name).suffix == ".ttf":
        return member
    return None


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
