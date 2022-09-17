#!/usr/bin/env zsh

DOTFILES_DIR="$(cd "$(dirname "$(dirname "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"
export DOTFILES_DIR

# Run everything in the base unix RC file.
_unixrc="${DOTFILES_DIR}/scripts/unixrc.sh"
if [ -f "${_unixrc}" ]; then
    . "${_unixrc}"
fi
unset _unixrc
