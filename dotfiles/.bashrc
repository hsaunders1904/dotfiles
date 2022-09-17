# Run everything in the base unix RC file.
_THIS_DIR="$(dirname "$(readlink -f "$0")")"
_unixrc="${_THIS_DIR}/unixrc.sh"
if [ -f "${_unixrc}" ]; then
    . "${_unixrc}"
fi
unset _unixrc
unset _THIS_DIR

# Custom prompt
_prompt_path="${DOTFILES_DIR}/scripts/prompt.sh"
if [ -f "${_prompt_path}" ]; then
        . "${_prompt_path}"
        PS1=$(get_prompt)
        export PS1
fi
unset _prompt_path
