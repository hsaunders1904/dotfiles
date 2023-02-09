#!/usr/bin/env zsh

DOTFILES_DIR="$(dirname "${0:a:h}")"
export DOTFILES_DIR

# oh-my-zsh settings
if [ -d "${HOME}/.oh-my-zsh" ]; then
    export ZSH="${HOME}/.oh-my-zsh"
    export ZSH_CUSTOM="${DOTFILES_DIR}/apps/oh-my-zsh"
    ZSH_THEME="custom_oxide"
    plugins=(
        autoupdate
        fd
        git
        copybuffer
        copyfile
        extract
        poetry
        rust
        zsh-autosuggestions
    )
    source "${ZSH}/oh-my-zsh.sh"
fi

_shrc="${DOTFILES_DIR}/dotfiles/.shrc"
if [ -f "${_shrc}" ]; then
    . "${_shrc}"
fi
unset _shrc

_aliases="${DOTFILES_DIR}/dotfiles/.zsh_aliases"
if [ -f "${_aliases}" ]; then
    . "${_aliases}"
fi
unset _aliases

_fzf_bindings="/usr/share/doc/fzf/examples/key-bindings.zsh"
if [ -f "${_fzf_bindings}" ]; then
    source "${_fzf_bindings}"
fi
unset _fzf_bindings
