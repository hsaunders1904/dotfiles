import os
from pathlib import Path

from installer.lib import REPO_ROOT, update_dotfile

__all__ = ["install"]

COMMENT_CHAR = "--"
RC_FILE = "init.lua"
THIS_RC_PATH = REPO_ROOT / "apps" / "neovim" / RC_FILE
IMPORT_TEMPLATE = (
    "do\n"
    "    local function file_exists(name)\n"
    "        local f = io.open(name, 'r')\n"
    "        if f ~= nil then io.close(f) return true else return false end\n"
    "    end\n"
    "    \n"
    "    local init = '{}'\n"
    "    if file_exists(init) then\n"
    "        dofile(init)\n"
    "    end\n"
    "end\n"
)


def install():
    config_path = nvim_init_path()
    config_path.parent.mkdir(parents=True, exist_ok=True)
    update_init_file(THIS_RC_PATH, str(config_path))


def update_init_file(this: Path, dot_file: Path):
    import_str = build_import_str(this)
    update_dotfile(dot_file, import_str, COMMENT_CHAR, new_line="\n")


def build_import_str(file_path: Path) -> str:
    return IMPORT_TEMPLATE.format(file_path)


def nvim_init_path() -> Path:
    if os.name == "nt":
        return (Path("~/AppData/Local/nvim") / RC_FILE).expanduser()
    xdg_config = Path(os.environ.get("XDG_CONFIG_HOME", "~/.config"))
    return (xdg_config / "nvim" / RC_FILE).expanduser()
