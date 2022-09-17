#!/usr/bin/env bash

function _get_git_branch() {
        local git_branch
        git_branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)"
        if [ "${git_branch}" != "" ]; then
                git_branch="[${git_branch}]"
                echo "${git_branch}"
        fi
}

function _get_conda_env() {
        conda_prompt="${CONDA_DEFAULT_ENV}"
        if [ "${conda_prompt}" != "" ] && [ "${conda_prompt}" != "base" ]; then
                conda_prompt="(${conda_prompt})"
                echo "${conda_prompt}"
        fi
}

function _view_tput_colours() {
        for ((i = 0; i < 17; i++)); do
                echo "$(tput setaf "$i")This is ($i) $(tput sgr0)"
        done
}

function get_prompt() {
        local -r light_blue="$(tput setaf 12)"
        local -r light_green="$(tput setaf 10)"
        local -r light_pink="\e[38;5;218m"
        local -r white="$(tput sgr0)"
        local -r cwd="\w"
        local -r user_name="\u"
        local -r host_name="\h"

        prompt="\[\e]0;\[${light_green}\]${user_name}@${host_name}"
        prompt+="\[${white}\]\$(echo \$(_get_conda_env))"
        prompt+="\[${white}\]:\[${light_blue}\]${cwd}"
        prompt+="\[${light_pink}\]\$(_get_git_branch)"
        prompt+="\[${white}\]$ "

        echo "${prompt}"
}
