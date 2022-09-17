DOTFILES_DIR="$(dirname "$(dirname "$(readlink -f "$0")")")"
export DOTFILES_DIR

# Path additions
if [ -d "${HOME}/.local/bin" ]; then
    export PATH="${HOME}/.local/bin:$PATH"
fi

# Tab-completion
if [ -x "$(command -v conda)" ]; then
    eval "$(register-python-argcomplete conda)"
fi
if [ -x "$(command -v gh)" ]; then
    eval "$(gh completion -s "$(basename "${SHELL}")")"
fi

# Setup z.sh
_z_path="${DOTFILES_DIR}/external/z.sh"
if [ -f "${_z_path}" ]; then
    . "${_z_path}"
fi
unset _z_path

# Import some functions - mostly more complex aliases
_funcs_path="${DOTFILES_DIR}/dotfiles/functions.sh"
if [ -f "${_funcs_path}" ]; then
    . "${_funcs_path}"
fi
unset _funcs_path

# Alias definitions
_aliases_path="${DOTFILES_DIR}/dotfiles/aliases.sh"
if [ -f "${_aliases_path}" ]; then
    . "${_aliases_path}"
fi
unset _aliases_path
