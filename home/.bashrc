#!/usr/bin/env bash

DOTFILES_DIR="$(cd "$(dirname "$(dirname "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"
export DOTFILES_DIR

_shrc="${DOTFILES_DIR}/home/.shrc"
if [ -f "${_shrc}" ]; then
    . "${_shrc}"
fi
unset _shrc

_funcs_path="${DOTFILES_DIR}/home/.bash_functions"
if [ -f "${_funcs_path}" ]; then
    . "${_funcs_path}"
fi
unset _funcs_path

# Custom prompt
_prompt_path="${DOTFILES_DIR}/home/.bash_prompt"
if [ -f "${_prompt_path}" ]; then
    . "${_prompt_path}"
    PS1=$(get_prompt)
    export PS1
fi
unset _prompt_path

_activations="${DOTFILES_DIR}/home/.activations"
if [ -f "${_activations}" ]; then
    . "${_activations}" "bash"
fi
unset _activations
