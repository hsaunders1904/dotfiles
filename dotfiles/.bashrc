# Run everything in the base unix RC file.
_THIS_DIR="$(dirname "$(readlink -f "$0")")"
_unixrc="${_THIS_DIR}/unixrc.sh"
if [ -f "${_unixrc}" ]; then
    . "${_unixrc}"
fi
unset _unixrc
unset _THIS_DIR
