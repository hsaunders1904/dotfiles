#!/usr/bin/env zsh

DOTFILES_DIR="$(dirname "${0:a:h}")"
export DOTFILES_DIR

_shrc="${DOTFILES_DIR}/home/.shrc"
if [ -f "${_shrc}" ]; then
    . "${_shrc}"
fi
unset _shrc

_aliases="${DOTFILES_DIR}/home/.zsh_aliases"
if [ -f "${_aliases}" ]; then
    . "${_aliases}"
fi
unset _aliases

# oh-my-zsh settings
if [ -d "${HOME}/.oh-my-zsh" ]; then
    export ZSH="${HOME}/.oh-my-zsh"
    export ZSH_CUSTOM="${DOTFILES_DIR}/home/.oh-my-zsh"
    ZSH_THEME="custom_oxide"
    plugins=(
        autoupdate
        copybuffer
        copyfile
        extract
        git
        poetry
        pyautoenv
        rust
        uv
        zsh-autosuggestions
    )
    source "${ZSH}/oh-my-zsh.sh"
fi

_activations="${DOTFILES_DIR}/home/.activations"
if [ -f "${_activations}" ]; then
    . "${_activations}" "zsh"
fi
unset _activations
