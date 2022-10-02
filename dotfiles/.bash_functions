#!/usr/bin/env bash

extract() {
    # Extract different types of files using the relevant tools
    if [ -f $1 ]; then
        case $1 in
        *.tar.bz2) tar xjf "$1" ;;
        *.tar.gz) tar xzf "$1" ;;
        *.bz2) bunzip2 "$1" ;;
        *.rar) rar x "$1" ;;
        *.gz) gunzip "$1" ;;
        *.tar) tar xf "$1" ;;
        *.tbz2) tar xjf "$1" ;;
        *.tgz) tar xzf "$1" ;;
        *.zip) unzip "$1" ;;
        *.Z) uncompress "$1" ;;
        *) echo "'$1' cannot be extracted via extract()" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}

noglob() {
    # Prevent globbing for the executed command; attempts to replicate the
    # equivalent zsh command.
    local noglob_set="${-//[^f]/}"
    if [ -n "${noglob_set}" ]; then
        set -f
    fi
    $@
    if [ -n "${noglob_set}" ]; then
        set +f
    fi
}
