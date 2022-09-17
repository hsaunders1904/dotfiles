#!/usr/bin/env bash

DOTFILES_DIR="$(cd "$(dirname "$(dirname "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"
export DOTFILES_DIR

_shrc="${DOTFILES_DIR}/dotfiles/.shrc"
if [ -f "${_shrc}" ]; then
    . "${_shrc}"
fi
unset _shrc

# Custom prompt
_prompt_path="${DOTFILES_DIR}/dotfiles/.bash_prompt"
if [ -f "${_prompt_path}" ]; then
        . "${_prompt_path}"
        PS1=$(get_prompt)
        export PS1
fi
unset _prompt_path
