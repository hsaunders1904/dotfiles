#!/usr/bin/env bash

DOTFILES_DIR="$(dirname "$(dirname "$(readlink -f "$0")")")"
export DOTFILES_DIR

# Run everything in the base unix RC file.
_unixrc="${DOTFILES_DIR}/scripts/unixrc.sh"
if [ -f "${_unixrc}" ]; then
    . "${_unixrc}"
fi
unset _unixrc

# Custom prompt
_prompt_path="${DOTFILES_DIR}/scripts/prompt.sh"
if [ -f "${_prompt_path}" ]; then
        . "${_prompt_path}"
        PS1=$(get_prompt)
        export PS1
fi
unset _prompt_path
