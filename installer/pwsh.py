import shutil
from pathlib import Path

from installer.base import Installer


class PwshInstaller(Installer):
    COMMENT_CHAR = "#"

    def install(self) -> bool:
        ok = self.install_modules()
        ok &= self.update_profile()
        return ok

    def should_install(self) -> bool:
        if not self.is_executable("pwsh"):
            self.logger().debug("skipping: 'pwsh' not found")
            return False
        if not self.dotfiles_profile_path().is_file():
            self.logger().debug(
                f"skipping: '{self.dotfiles_profile_path()}' is not a file"
            )
            return False
        return True

    def update_profile(self) -> bool:
        if not (pwsh_profile := self.profile_path()):
            self.logger().warning("could not get path to pwsh profile")
            return False
        dotfile = self.dotfiles_profile_path()
        import_str = "\n".join(
            [
                f'if (Test-Path "{dotfile}") {{',
                f'    . "{dotfile}"',
                "}",
            ]
        )
        return self.update_dotfile(pwsh_profile, import_str, self.COMMENT_CHAR)

    def install_modules(self) -> bool:
        if not (pwsh_exe := self.pwsh_exe()):
            self.logger().debug("could not install modules, pwsh not found")
            return False
        install_script = (
            self.repo_root() / "installer" / "scripts" / "install_modules.ps1"
        )
        cmd = [
            str(pwsh_exe),
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-Command",
            f'. "{install_script}"',
        ]
        return self.run_command(cmd)

    def profile_path(self) -> Path | None:
        if not (pwsh_exe := self.pwsh_exe()):
            return None
        args = [
            str(pwsh_exe),
            "-NoProfile",
            "-Command",
            r"Write-Host $PROFILE",
        ]
        if profile_str := self.run_command_get_output(args, log=False):
            return Path(profile_str.strip())
        return None

    def dotfiles_profile_path(self) -> Path:
        return (
            self.dotfiles_home()
            / ".config"
            / "powershell"
            / "Microsoft.PowerShell_profile.ps1"
        )

    def pwsh_exe(self) -> Path | None:
        if pwsh_exe := shutil.which("pwsh"):
            return Path(pwsh_exe)
        return None
