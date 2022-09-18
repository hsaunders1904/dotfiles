from installer import lib

Z_JUMP_AROUND_URL = "https://raw.githubusercontent.com/rupa/z/master/z.sh"


def download_z_jump_around(download_loc: str):
    lib.download_file(Z_JUMP_AROUND_URL, download_loc)


if __name__ == "__main__":
    download_z_jump_around("z.sh")
