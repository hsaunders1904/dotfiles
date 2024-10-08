# Oxide theme for Zsh
#
# Author: Diki Ananta <diki1aap@gmail.com>
# Edited by: Harry Saunders <33317174+hsaunders1904@users.noreply.github.com>
# Repository: https://github.com/dikiaap/dotfiles
# License: MIT

# Prompt:
# %F => Color codes
# %f => Reset color
# %~ => Current path
# %(x.true.false) => Specifies a ternary expression
#   ! => True if the shell is running with root privileges
#   ? => True if the exit status of the last command was success
#
# Git:
# %a => Current action (rebase/merge)
# %b => Current branch
# %c => Staged changes
# %u => Unstaged changes
#
# Terminal:
# \n => Newline/Line Feed (LF)

setopt PROMPT_SUBST

autoload -U add-zsh-hook
autoload -Uz vcs_info

# Use True color (24-bit) if available.
oxide_white="%F{white}"
if [[ "${terminfo[colors]}" -ge 256 ]]; then
    oxide_turquoise="%F{73}"
    oxide_orange="%F{179}"
    oxide_red="%F{167}"
    oxide_limegreen="%F{107}"
    oxide_yellow="%F{227}"
else
    oxide_turquoise="%F{cyan}"
    oxide_orange="%F{yellow}"
    oxide_red="%F{red}"
    oxide_limegreen="%F{green}"
    oxide_yellow="%F{yellow}"
fi

# Reset color.
oxide_reset_color="%f"

# VCS style formats.
FMT_UNSTAGED="%{$oxide_reset_color%} %{$oxide_orange%}●"
FMT_STAGED="%{$oxide_reset_color%} %{$oxide_limegreen%}✚"
FMT_ACTION="(%{$oxide_limegreen%}%a%{$oxide_reset_color%})"
FMT_VCS_STATUS="on %{$oxide_turquoise%} %b%u%c%{$oxide_reset_color%}"

zstyle ':vcs_info:*' enable git svn
zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:*' unstagedstr    "${FMT_UNSTAGED}"
zstyle ':vcs_info:*' stagedstr      "${FMT_STAGED}"
zstyle ':vcs_info:*' actionformats  "${FMT_VCS_STATUS} ${FMT_ACTION}"
zstyle ':vcs_info:*' formats        "${FMT_VCS_STATUS}"
zstyle ':vcs_info:*' nvcsformats    ""
zstyle ':vcs_info:git*+set-message:*' hooks git-untracked

# Check for untracked files.
+vi-git-untracked() {
    if [[ $(git rev-parse --is-inside-work-tree 2> /dev/null) == 'true' ]] && \
            git status --porcelain | grep --max-count=1 '^??' &> /dev/null; then
        hook_com[staged]+="%{$oxide_reset_color%} %{$oxide_red%}●"
    fi
}

# Executed before each prompt.
add-zsh-hook precmd vcs_info

function _get_python_env() {
    # Prioritise venvs over conda, as we could be in a venv within conda
    if [ -n "${VIRTUAL_ENV}" ]; then
        py_env="$(basename "${VIRTUAL_ENV}")"
        is_poetry=$(! [[ "$(dirname "${VIRTUAL_ENV}")" = */pypoetry/virtualenvs ]]; echo $?)
        if ! ((is_poetry)); then
            py_env="$(basename "$(dirname "${VIRTUAL_ENV}")")/${py_env}"
        fi
    elif [ -n "${CONDA_DEFAULT_ENV}" ] && [ "${CONDA_DEFAULT_ENV}" != "base" ]; then
        py_env="${CONDA_DEFAULT_ENV}"
    fi
    if [ -n "${py_env}" ]; then
        echo "(\ue235 ${py_env}) "
    fi
}

function _get_dstask_count() {
    if command -v dstask >/dev/null 2>&1; then
        TASK_COUNT="$(dstask | grep '"id"' --count)"
        if ! [ "$TASK_COUNT" -eq "0" ]; then
            echo "${TASK_COUNT}📝 "
        fi
    fi
}

# Stop Python virtual environments from editing prompt
export VIRTUAL_ENV_DISABLE_PROMPT=1

PROMPT=$'\n'
PROMPT+=$'%{$oxide_limegreen%}%/%{$oxide_reset_color%} '
PROMPT+=$'%{$oxide_red%}$(_get_dstask_count)%{$oxide_reset_color%}'
PROMPT+=$'%{$oxide_yellow%}$(_get_python_env)%{$oxide_reset_color%}'
PROMPT+=$'${vcs_info_msg_0_}\n'
PROMPT+=$'%(?.%{$oxide_white%}.%{$oxide_red%})%(!.#.»)%{$oxide_reset_color%} '
