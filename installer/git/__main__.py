if __name__ == "__main__":
    # I don't want to have to pip install this installer.
    # Manually add paths instead.
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent.parent.parent))

    from _install import install

    install()
