DOTFILES_DIR="$(dirname "$(dirname "$(readlink -f "$0")")")"
export DOTFILES_DIR

# Run everything in the base unix RC file.
_unixrc="${DOTFILES_DIR}/scripts/unixrc.sh"
if [ -f "${_unixrc}" ]; then
    . "${_unixrc}"
fi
unset _unixrc
