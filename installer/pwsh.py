import os
import shutil
import subprocess

from installer import lib

__all__ = ["install"]

PWSH_COMMENT_CHAR = "#"
THIS_DIR = os.path.dirname(__file__)
THIS_PWSH_PROFILE = os.path.join(lib.REPO_ROOT, "dotfiles", ".pwsh_profile.ps1")


def install():
    install_module_dependencies()
    update_profile()


def update_profile() -> None:
    import_str = _build_import_str(THIS_PWSH_PROFILE)
    pwsh_profile = _get_pwsh_profile_path()
    if not os.path.isdir(os.path.dirname(pwsh_profile)):
        os.makedirs(os.path.dirname(pwsh_profile), exist_ok=True)
    lib.update_dotfile(pwsh_profile, import_str, PWSH_COMMENT_CHAR)


def install_module_dependencies():
    install_script = os.path.join(THIS_DIR, "scripts", "install_modules.ps1")
    cmd = [
        shutil.which("pwsh"),
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-Command",
        f'. "{install_script}"',
    ]
    lib.run_command(cmd)


def _get_pwsh_profile_path() -> str:
    raw_output = subprocess.check_output(
        [
            shutil.which("pwsh"),
            "-NoProfile",
            "-Command",
            r"Write-Host $PROFILE",
        ]
    )
    return raw_output.decode().strip()


def _build_import_str(file_to_import: str, tab_size: int = 2) -> str:
    return (
        f'if (Test-Path "{file_to_import}") {{\n'
        f'{" " * tab_size}. "{file_to_import}"\n'
        f"}}"
    )
