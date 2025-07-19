import os
from pathlib import Path

from installer.base import Installer


class NeovimInstaller(Installer):
    COMMENT_CHAR = "--"
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
        "end"
    )

    def install(self) -> bool:
        return self.update_init_lua()

    def should_install(self) -> bool:
        return self.is_executable("nvim")

    def update_init_lua(self) -> bool:
        dotfile_path = self.repo_root() / "apps" / "neovim" / "init.lua"
        import_str = self.IMPORT_TEMPLATE.format(dotfile_path)
        path = self.init_lua_path()
        path.parent.mkdir(exist_ok=True, parents=True)
        return self.update_dotfile(path, import_str, self.COMMENT_CHAR)

    def init_lua_path(self) -> Path:
        if os.name == "nt":
            return (Path("~/AppData/Local/nvim") / "init.lua").expanduser()
        xdg_config = Path(os.environ.get("XDG_CONFIG_HOME", "~/.config"))
        return (xdg_config / "nvim" / "init.lua").expanduser()
