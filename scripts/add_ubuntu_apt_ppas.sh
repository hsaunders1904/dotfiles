#!/usr/bin/env bash

set -o errexit # exit early on any error
set -o nounset # raise error using unused variables

ubuntu_release="$(lsb_release -cs)"

# Kitware (for CMake)
wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | sudo tee /usr/share/keyrings/kitware-archive-keyring.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu/ ${ubuntu_release} main" |
    sudo tee /etc/apt/sources.list.d/kitware.list >/dev/null
sudo apt update
sudo rm /usr/share/keyrings/kitware-archive-keyring.gpg
sudo apt install kitware-archive-keyring

# GitHub CLI
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg |
    sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" |
    sudo tee /etc/apt/sources.list.d/github-cli.list >/dev/null

sudo apt update
