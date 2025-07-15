from installer.base import Installer


class GitInstaller(Installer):
    def install(self) -> bool:
        self.add_config_include_path()
        self.add_config_excludesfile()
        return True

    def add_config_include_path(self):
        path = self.repo_root() / "dotfiles" / ".gitconfig"
        self.set_config_option_value("include.path", str(path))

    def add_config_excludesfile(self):
        excludes_file = self.repo_root() / "dotfiles" / ".gitignore_global"
        self.set_config_option_value("core.excludesfile", str(excludes_file))

    def set_config_option_value(self, option: str, value: str):
        current_values = self.get_config_option_values(option)
        if value in current_values:
            return
        args = ["git", "config", "--global", "--add", option, value]
        self.run_command(args)

    def get_config_option_values(self, option: str) -> list[str]:
        args = ["git", "config", "--global", "--get-all", option]
        return self.run_command_get_output(args, log=False).strip().split("\n")
