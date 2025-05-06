import platform
import sys
from pathlib import Path

DOTFILES_DIR = Path(__file__).parent.parent
sys.path.append(str(DOTFILES_DIR))


def install():
    import scripts.nerdfont as nf

    if platform.system() == "Darwin":
        fonts = ["LiberationMono"]
        print(f"[+] Installing Nerd Fonts: {fonts}")
        nf.install_fonts(fonts)
    elif platform.system() == "Linux":
        fonts = ["UbuntuMono"]
        print(f"[+] Installing Nerd Fonts: {fonts}")
        nf.install_fonts(fonts)
