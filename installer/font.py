import platform
import sys

from installer.base import Installer


class FontInstaller(Installer):
    def install(self) -> bool:
        sys.path.append(str(self.repo_root()))
        import scripts.nerdfont as nf

        nf.logger.handlers = []
        for handler in self.logger().handlers:
            nf.logger.addHandler(handler)
        nf.logger.propagate = False
        self.logger().propagate = False

        ok = False
        if platform.system() == "Darwin":
            fonts = ["LiberationMono", "SourceCodePro"]
            ok = nf.install_fonts(fonts)
        elif platform.system() == "Linux":
            fonts = ["UbuntuMono"]
            ok = nf.install_fonts(fonts)
        return ok

    def should_install(self) -> bool:
        return platform.system() in ["Darwin", "Linux"]
