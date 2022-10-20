import os
import subprocess

from installer import lib

__all__ = ["install"]

CUSTOM_ZSH_DIR = os.path.join(lib.REPO_ROOT, "apps", "oh-my-zsh")
SH_COMMENT_CHAR = "#"
HOME_ZSH_PATH = os.path.join(os.path.expanduser("~"), ".zshrc")
THIS_ZSH_PATH = os.path.join(lib.REPO_ROOT, "dotfiles", ".zshrc")
OHMYZSH_URL = "https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh"


def install():
    pull_plugins()
    update_zshrc()
    if not ohmyzsh_installed():
        install_ohmyzsh()
    else:
        print("[-] oh-my-zsh already installed")


def update_zshrc():
    import_str = build_file_import_str(THIS_ZSH_PATH)
    lib.update_dotfile(HOME_ZSH_PATH, import_str, SH_COMMENT_CHAR, new_line="\n")


def ohmyzsh_installed():
    path = os.environ.get("ZSH", None)
    if path is not None:
        return os.path.isdir(path)
    return False


def install_ohmyzsh():
    installer_path = os.path.join(lib.REPO_ROOT, "external", "ohmyzsh_install.sh")
    lib.download_file(OHMYZSH_URL, installer_path, log=False)
    install_cmd = ["sh", installer_path, "--unattended", "--keep-zshrc"]
    print(f"[+] {' '.join(install_cmd)}")
    result = subprocess.run(install_cmd, stdout=subprocess.PIPE)
    if result.returncode != 0:
        print(result.stdout.decode())


def build_file_import_str(file_path: str):
    return f'if [ -f "{file_path}" ]; then\n' f'    . "{file_path}"\n' f"fi"


def pull_plugins():
    cmd = ["git", "submodule", "update", "--init", CUSTOM_ZSH_DIR]
    lib.run_command(cmd)
