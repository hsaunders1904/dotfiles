# dotfiles

Dotfiles and configs for various shells, apps, and OSes.

## Install

The installer works by importing this repository's dotfiles from within existing user dotfiles.
If no existing dotfiles exist, new ones are created.
This allows keeping machine-specific configuration in user dotfiles
(e.g., in `${HOME}/.bashrc`).

Install requires Python (>=3.6).

### Linux

- If using Ubuntu, install dependencies using `apt`.

    ```console
    sudo apt install ./apt-list.txt
    ```

    If using some other Linux flavour,
    install the dependencies in whichever other way you like.

- Run the installer module.

    ```console
    python3 -m installer
    ```

### MacOS

- Install dependencies using `Brewfile`.

    ```console
    brew bundle
    ```

- Run the installer module.

    ```console
    python3 -m installer
    ```


### Windows

- Install [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/).
- Install required packages.

    ```console
    powershell.exe -Command "winget install $(Get-Content ./winget-list.txt)"
    ```
- Run installer module.

    ```console
    python -m installer
    ```
