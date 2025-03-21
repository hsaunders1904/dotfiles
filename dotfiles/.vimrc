filetype indent on
filetype plugin indent on   " allow auto-indenting depending on file type
filetype plugin on

syntax on                   " syntax highlighting

set termguicolors
colorscheme desert

set autoindent              " indent a new line the same amount as the line just typed
set backupdir=~/.cache/vim  " Directory to store backup files.
set clipboard=unnamedplus   " using system clipboard
set cursorline              " highlight current cursorline
set expandtab               " converts tabs to white space
set hlsearch                " highlight search
set ignorecase              " case insensitive
set incsearch               " incremental search
set mouse=a                 " enable mouse click
set mouse=v                 " middle-click paste
set nocompatible            " disable compatibility to old-time vi
set noswapfile
set number                  " add line numbers
set relativenumber
set ruler
set shiftwidth=4            " width for autoindents
set showmatch               " show matching
set softtabstop=4           " see multiple spaces as tabstops so <BS> does the right thing
set spell                   " enable spell check (may need to download language package)
set spelllang=en
set tabstop=4               " number of columns occupied by a tab
set ttyfast                 " Speed up scrolling
set wildmode=longest,list   " get bash-like tab completions

let mapleader = " "
let maplocalleader = "\\"
nnoremap <leader>w :w<CR>
nnoremap <leader>qq :q<CR>

hi clear spellbad
hi spellbad gui=underline,italic cterm=underline,italic term=underline,italic
hi cursorline guibg=Grey20
