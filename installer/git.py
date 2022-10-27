import os

from installer import lib

__all__ = ["install"]

CONFIG_FILE_NAME = ".gitconfig"
IGNORE_FILE_NAME = ".gitignore_global"
DOTFILES_DIR = os.path.join(lib.REPO_ROOT, "dotfiles")


def install():
    add_config_include_path()
    add_config_excludesfile()


def get_config_option_values(option):
    args = ["git", "config", "--global", "--get-all", option]
    return lib.run_command_get_output(args, log=False).strip().split("\n")


def set_config_option_value(option, value):
    current_values = get_config_option_values(option)
    if value in current_values:
        return
    args = ["git", "config", "--global", "--add", option, value]
    lib.run_command(args)


def add_config_include_path():
    path = os.path.join(DOTFILES_DIR, CONFIG_FILE_NAME)
    if os.path.isfile(path):
        set_config_option_value("include.path", path)


def add_config_excludesfile():
    path = os.path.join(DOTFILES_DIR, IGNORE_FILE_NAME)
    if os.path.isfile(path):
        set_config_option_value("core.excludesfile", path)
