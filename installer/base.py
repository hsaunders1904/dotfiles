"""Base class for installer definitions."""

import abc
import logging
import re
import shutil
import subprocess
from pathlib import Path
from urllib import request

from installer.logging import make_logger

logger = make_logger("dotfiles")


class Installer(abc.ABC):
    REGION_START = ">>> hsaunders1904/dotfiles >>>"
    REGION_END = "<<< hsaunders1904/dotfiles <<<"

    def __init__(self, dry_run: bool = False) -> None:
        self.dry_run = dry_run

    @abc.abstractmethod
    def install(self) -> bool:
        """Run the install steps for the installer instance."""

    def should_install(self) -> bool:
        return True

    def repo_root(self) -> Path:
        return Path(__file__).parent.parent

    def dotfiles_home(self) -> Path:
        return Path(__file__).parent.parent / "home"

    def external_dir(self) -> Path:
        return self.repo_root() / "external"

    @staticmethod
    def is_executable(exe_name: str) -> bool:
        return shutil.which(exe_name) is not None

    def update_dotfile(self, path: Path, new_content: str, comment_char: str) -> bool:
        logger.info("DOTFILE: updating '%s'", path)
        if self.dry_run:
            return True
        if (file_content := _read_file_if_exists(path)) is None:
            return False
        new_content = _update_dotfile_region(
            file_content,
            new_content,
            comment_char,
            (self.REGION_START, self.REGION_END),
        )
        if new_content is not None:
            with path.open("w") as f_writer:
                f_writer.write(new_content)
        return True

    def run_command(self, args: list[str], **kwargs) -> bool:
        cmd_str = " ".join(args)
        logger.info("RUN: %s", cmd_str)
        if self.dry_run:
            return True

        result = subprocess.run(args, capture_output=True, text=True, **kwargs)

        level = logging.WARNING if result.returncode != 0 else logging.DEBUG
        for name, content in [("STDOUT", result.stdout), ("STDERR", result.stderr)]:
            if content:
                logger.log(level, "RUN %s:\n%s", name, content)

        return result.returncode == 0

    def run_command_get_output(self, args: list[str], *, log=True, **kwargs) -> str:
        if log:
            logger.info("RUN: %s", " ".join(args))
        if self.dry_run:
            return ""
        result = subprocess.run(args, stdout=subprocess.PIPE, **kwargs)
        return result.stdout.decode()

    def download_file(self, url: str, out_path: Path, force: bool = False) -> bool:
        if not force and out_path.is_file():
            logger.info("DOWNLOAD: skipped '%s' already exists", out_path)
            return False
        logger.info("DOWNLOAD: '%s' -> '%s'", url, out_path)
        if self.dry_run:
            return True
        try:
            _download(url, out_path)
            return True
        except Exception:
            logging.exception("DOWNLOAD: failed")
            return False

    def make_symlink(self, origin: Path, link: Path) -> bool:
        if link.is_file():
            logger.info("SYMLINK: link '%s' is already a file or symlink", link)
            return True
        logger.info("SYMLINK: '%s' -> '%s'", origin, link)
        return self.run_command(["ln", "-s", str(origin), str(link)])

    def git_clone(self, url: str, path: Path) -> bool:
        logger.info("GIT: cloning '%s' into '%s'", url, path)
        return self.run_command(["git", "clone", url, str(path)])

    def git_pull(self, repo_dir: Path) -> bool:
        logger.info("GIT: pulling '%s'", repo_dir)
        return self.run_command(["git", "-C", str(repo_dir), "pull"])

    def logger(self) -> logging.Logger:
        return logger

    @staticmethod
    def local_bin() -> Path:
        return Path.home() / ".local" / "bin"


def _download(url: str, out_path: Path):
    request.urlretrieve(url, out_path)


def _read_file_if_exists(file_path: Path) -> str | None:
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""
    except OSError:
        logging.exception("could not read file '%s'", file_path)
        return None


def _update_dotfile_region(
    string: str, new_content: str, comment_char: str, region_delimiters: tuple[str, str]
):
    region_start, region_end = region_delimiters
    region_re = (
        f"{comment_char} *{region_start}\n"
        r"([\s\S]*)\n"
        f"{comment_char} *{region_end}\n"
    )
    re_pattern = re.compile(region_re, re.MULTILINE)
    match = re_pattern.search(string)

    new_content.removesuffix("\n")
    new_region = "\n".join(
        [
            f"{comment_char} {region_start}",
            f"{new_content}",
            f"{comment_char} {region_end}",
            "",
        ]
    )
    if match:
        # escape backlashes, particularly important for Windows paths
        return re_pattern.sub(new_region.replace("\\", "\\\\"), string)
    else:
        if string == "":
            return new_region
        else:
            return f"{string}\n{new_region}"
