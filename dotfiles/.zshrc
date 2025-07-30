#!/usr/bin/env zsh

DOTFILES_DIR="$(dirname "${0:a:h}")"
export DOTFILES_DIR

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

# oh-my-zsh settings
if [ -d "${HOME}/.oh-my-zsh" ]; then
    export ZSH="${HOME}/.oh-my-zsh"
    export ZSH_CUSTOM="${DOTFILES_DIR}/apps/oh-my-zsh"
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

if [ -f "/opt/homebrew/opt/fzf/shell/key-bindings.zsh" ]; then
    source "/opt/homebrew/opt/fzf/shell/key-bindings.zsh"
elif [ -d "${DOTFILES_DIR}/external/fzf" ]; then
    if [[ $- == *i* ]]; then
        source "${DOTFILES_DIR}/external/fzf/shell/completion.zsh" 2>/dev/null
    fi
    source "${DOTFILES_DIR}/external/fzf/shell/key-bindings.zsh"
fi
