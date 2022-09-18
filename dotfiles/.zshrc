#!/usr/bin/env zsh

DOTFILES_DIR="$(dirname "${0:a:h}")"
export DOTFILES_DIR

_shrc="${DOTFILES_DIR}/dotfiles/.shrc"
if [ -f "${_shrc}" ]; then
    . "${_shrc}"
fi
unset _shrc

# oh-my-zsh settings
if [ -d "${HOME}/.oh-my-zsh" ]; then
    export ZSH="${HOME}/.oh-my-zsh"
    export ZSH_CUSTOM="${DOTFILES_DIR}/.oh-my-zsh"
    ZSH_THEME="custom_oxide"
    plugins=(git copyfile)
    source ${ZSH}/oh-my-zsh.sh
fi

# ls file/directory colours
# ow and tw change symlinks, and di changes directory colours
# export LS_COLORS="$LS_COLORS:ow=1;94:tw=1;94:di=38;5;213:ex=0;32"
export LS_COLORS="$LS_COLORS:di=38;5;213"
