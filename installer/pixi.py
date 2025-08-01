import os
import shutil
from datetime import datetime
from hashlib import sha1
from pathlib import Path

from installer.base import Installer


class PixiInstaller(Installer):
    def install(self) -> bool:
        pixi_exe = Path.home() / ".pixi" / "bin" / "pixi"
        if not pixi_exe.is_file():
            if not self.linux_install():
                return False

        manifest = Path.home() / ".pixi" / "manifests" / "pixi-global.toml"
        manifest.parent.mkdir(exist_ok=True)
        dotfile_manifest = (
            self.dotfiles_home() / ".pixi" / "manifests" / "pixi-global.toml"
        )
        self.make_symlink(dotfile_manifest, manifest, force=True)

        ok = self.run_command([str(pixi_exe), "global", "sync"])
        os.environ["PATH"] = ":".join(
            [str(pixi_exe.parent), *os.environ.get("PATH", "").split(":")]
        )
        return ok

    def should_install(self) -> bool:
        return True

    def linux_install(self) -> bool:
        installer_path = Path("/tmp") / "pixi_install.sh"
        if not self.download_file(
            "https://pixi.sh/install.sh", installer_path, force=True
        ):
            return False

        if not self.run_command(
            ["sh", str(installer_path)], env=os.environ | {"PIXI_NO_PATH_UPDATE": "1"}
        ):
            return False
        return True


def file_are_equal(a: Path, b: Path):
    return _sha256_file(a) == _sha256_file(b)


def _backup_and_move(path: Path) -> Path:
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    new_path = path.with_name(path.name + current_time + ".bak")
    return Path(shutil.move(path, new_path))


def _sha256_file(path: Path) -> bytes:
    BUF_SIZE = 65536  # 64kb
    hash = sha1()
    with path.open("rb") as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            hash.update(data)
    return hash.digest()
