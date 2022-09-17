function addpath() {
    # Add given paths to system path
    _new_path="$("${DOTFILES_DIR}/scripts/sys_path_append" "$@")"
    if [ -n "${_new_path}" ]; then
        export PATH="${_new_path}"
    fi
}

function bak() {
    # Create backups of the given files
    for path in "$@"; do
        cp "${path}" "${path}.bak"
    done
}

function cd_and_ls() {
    # Change directory and print its contents
    new_dir="$*"
    if [ $# -lt 1 ]; then
        new_dir=$HOME
    fi
    builtin cd "${new_dir}" && ls
}

function cpath() {
    # Copy the given file's full path to the clipboard
    if [ "$1" = "" ]; then
        _path="$(pwd)"
    else
        _path="$(realpath "$1")"
    fi

    if [ -n "$(command -v xclip)" ]; then
        echo -n "${_path}" | xclip -selection c && \
            echo "'${_path}' copied to clipboard"
    elif [ -n "$(command -v pbcopy)" ]; then
        echo -n "${_path}" | pbcopy && \
            echo "'${_path}' copied to clipboard"
    else
        echo "Could not find 'xlcip' or 'pbcopy' to copy path."
        return
    fi
}

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

function mkdir_and_cd() {
    # Make a directory and cd into it
    mkdir "$1"
    cd "$1" || return
}
