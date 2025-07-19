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
logger.setLevel(logging.INFO)


@dataclass
class CliArgs:
    fonts: list[str]


class Os(enum.Enum):
    LINUX = enum.auto()
    MACOS = enum.auto()


def main(argv: list[str]) -> int:
    """Download and install nerd fonts."""
    args = parse_args(argv)
    if install_fonts(args.fonts):
        return 0
    return 1


def install_fonts(font_names: list[str]) -> bool:
    if not (operating_system := get_os()):
        return False
    ok = True
    for font in font_names:
        url = f"{BASE_DOWNLOAD_URL}/{font}.tar.xz"
        if out_dir := get_fonts_dir(font, operating_system):
            out_dir.parent.mkdir(exist_ok=True, parents=True)
            ok &= download_and_extract_tar(url, out_dir)
    return ok


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


def get_os() -> Os | None:
    if sys.platform.startswith("linux"):
        return Os.LINUX
    if sys.platform.startswith("darwin"):
        return Os.MACOS
    logger.error("unsupported platform '%s'", sys.platform)
    return None


def download_and_extract_tar(url: str, out_dir: Path) -> bool:
    """Download and extract a nerd font into the given directory."""
    logger.info("downloading '%s'", url)
    try:
        with (
            request.urlopen(url) as response,
            tarfile.open(fileobj=response, mode="r|xz") as tar,
        ):
            logger.info("extracting to '%s'", out_dir)
            tar.extractall(out_dir, filter=_tar_filter)
    except Exception:
        logger.exception("failed to install '%s'", url)
        return False
    return True


def _tar_filter(member: tarfile.TarInfo, path: str, /) -> tarfile.TarInfo | None:
    member = tarfile.tar_filter(member, dest_path=path)
    member = tarfile.data_filter(member, dest_path=path)
    if Path(member.name).suffix in [".ttf", ".otf"]:
        return member
    return None


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
