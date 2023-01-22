import json
import os
from pathlib import Path
from typing import Union
from urllib import request
from zipfile import ZipFile

LOCAL_APP_DATA = "LOCALAPPDATA"
URL = "https://api.github.com/repos/sharkdp/fd"


def get_download_url() -> Union[str, None]:
    response = request.urlopen(f"{URL}/releases/latest")
    data = json.loads(response.read().decode())
    for asset in data["assets"]:
        if "x86_64-pc-windows-msvc.zip" in asset["name"]:
            return asset["browser_download_url"]
    return None


def download_zip() -> str:
    download_url = get_download_url()
    return request.urlretrieve(download_url)[0]


def extract_without_top_level(archive: str, out_dir: Path):
    with ZipFile(archive) as zip_file:
        for name in zip_file.namelist():
            # remove the first dir in the path, the 'fd-vX.X.X-x86...' part
            path = Path(*Path(name).parts[1:])
            path = out_dir / path
            if zip_file.getinfo(name).is_dir():
                path.mkdir()
            else:
                with zip_file.open(name, "r") as zip_f:
                    with open(path, "wb") as f:
                        f.write(zip_f.read())


def install():
    if os.name != "nt":
        return
    print("[+] Installing 'fd'...")
    local_app_data = os.getenv(LOCAL_APP_DATA)
    if local_app_data is None:
        return
    out_dir = Path(local_app_data, "Programs", "fd")
    out_dir.mkdir(exist_ok=True)
    archive = download_zip()
    if archive is None:
        return
    extract_without_top_level(archive, out_dir)
