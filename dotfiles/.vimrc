colorscheme slate

filetype indent on
filetype on
filetype plugin on

set expandtab

set hlsearch
set ignorecase
set incsearch
set nocompatible
set noswapfile
set number
set ruler
set shiftwidth=4
set spell
set spelllang=en
set t_te=^[[?47l    " on exit, pop terminal state from alternate screen
set t_ti=^[[?47h    " on init, push terminal state to alternate screen
set tabstop=4
if !has('nvim')
    set term=xterm-256color
endif

if has('nvim')
    :hi CocErrorHighlight gui=undercurl guisp=red
else
    :hi CocErrorHighlight cterm=undercurl ctermul=red
endif

syntax on

" Make misspelled words red and italic
hi clear SpellBad
hi SpellBad cterm=italic,underline

let mapleader = "'"

nmap <C-d> mzyyp`z
