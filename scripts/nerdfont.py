#!/usr/bin/env python3
"""
Download and install Nerd Fonts on Windows, Linux or MacOS.

https://www.nerdfonts.com/
"""

import argparse
import gzip
import logging
import sys
import tarfile
from collections.abc import Iterator
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import TextIO
from urllib import request

BASE_DOWNLOAD_URL = "https://github.com/ryanoasis/nerd-fonts/releases/latest/download"
LINUX_FONT_INSTALL_DIR = Path("~/.local/share/fonts").expanduser()

logger = logging.getLogger("nerdfont")


@dataclass
class CliArgs:
    fonts: list[str]


def main(argv: list[str]) -> int:
    """Download and install nerd fonts."""
    args = parse_args(argv)
    tmp_dir = Path(tmp_dir_str)
    for font in args.fonts:
        if not (font_archive := download_font_archive(font, out_dir=tmp_dir)):
            continue

    return 0


def parse_args(argv: list[str]) -> CliArgs:
    parser = argparse.ArgumentParser(
        "nerdfont",
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("fonts", nargs="+", help="the names of the fonts to install")
    return CliArgs(**vars(parser.parse_args(argv)))


def download_and_extract_tar(url: str, out_dir: Path):
    with (
        request.urlopen(url) as response,
        tarfile.open(fileobj=response, mode="r|xz") as tar,
    ):
        tar.extractall(out_dir)


def download_font_archive(font_name: str, out_dir: Path) -> Path | None:
    """
    Download a font and return the path it was downloaded to.

    Return ``None`` if the download failed.
    """
    if sys.platform.startswith("linux"):
        url = f"{BASE_DOWNLOAD_URL}/{font_name}.tar.gz"
    else:
        raise NotImplementedError
    out_path = out_dir / f"{font_name}"
    if download(url, out_path):
        return out_path
    return None


def iter_download(
    url: str, out_stream: BytesIO, chunk_size: int = 8192
) -> Iterator[None]:
    """
    Download the file to the destination path.

    Return ``True`` if the download succeeded.
    """
    progress_bar = _DownloadProgressBar(url.split("/")[-1], sys.stdout)
    try:
        with request.urlopen(url) as response:
            total_size = int(response.getheader("Contest-Length", 0))
            block_num = 0
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                out_stream.write(chunk)
                block_num += 1
                progress_bar(block_num=1, block_size=len(chunk), total_size=total_size)
                yield
    except Exception:
        logger.exception("could not download '%s'", url)
        raise StopIteration


class _DownloadProgressBar:
    """A simple progress bar."""

    def __init__(self, prefix: str, stdout: TextIO = sys.stdout) -> None:
        self.prefix = prefix
        self.stdout = stdout

    def __call__(self, block_num: int, block_size: int, total_size: int) -> None:
        """
        Flush stdout and print the state of the progress bar.

        This can be used as a callback function for urlretrieve's
        `reporthook`.
        """
        bar_len = 38
        num_blocks = max(total_size / block_size, 1)
        percentage = float(block_num) / num_blocks
        num_full = int(bar_len * percentage)
        self.stdout.write("\r")
        self.stdout.write(
            f"{self.prefix} [{'#' * num_full}{' ' * (bar_len - num_full)}] "
            f"{min(int(percentage * 100), 100)}%",
        )
        self.stdout.flush()


if __name__ == "__main__":
    # sys.exit(main(sys.argv[1:]))
    out_dir = Path.cwd() / "UbuntuMono"
    out_dir.mkdir(exist_ok=True)
    download_and_extract_tar(
        "https://github.com/ryanoasis/nerd-fonts/releases/latest/download/UbuntuMono.tar.xz",
        out_dir,
    )
