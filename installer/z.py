import os

from installer import lib

__all__ = ["install"]

Z_JUMP_AROUND_URL = "https://raw.githubusercontent.com/rupa/z/master/z.sh"


def install():
    out_path = os.path.join(lib.EXTERNAL_DIR, "z.sh")
    if not os.path.isfile(out_path):
        lib.download_file(Z_JUMP_AROUND_URL, out_path)
