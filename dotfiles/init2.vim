set nocompatible
filetype off

source ${DOTFILES_DIR}/external/plug.vim
call plug#begin()

  " Language server and highlighting
  Plug 'neovim/nvim-lspconfig'

  " Autocomplete
  Plug 'ms-jpq/coq_nvim', {'branch': 'coq'}

call plug#end()

if !empty('$DOTFILES_DIR')
  exe 'set runtimepath+=' . '$DOTFILES_DIR/apps/neovim'
endif

syntax on
set nowrap
set encoding=utf8
set number
set relativenumber
set completeopt=menu,menuone,noselect
set tabstop=4
set shiftwidth=4
set scrolloff=5
set background=dark
set spell
colorscheme gruvbox

hi clear spellbad
hi spellbad gui=underline,italic cterm=underline,italic term=underline,italic

" mouse movement
set mouse=a
" yanking and pasting from/to clipboard
set clipboard+=unnamedplus

" https://vim.fandom.com/wiki/Highlight_unwanted_spaces
" Highlight for weird whitespace:
:highlight ExtraWhitespace ctermbg=darkgreen guibg=darkgreen
" match trailing whitespace while not typing on that line, spaces before a tab
" and tabs not at the start of lines
:match ExtraWhitespace /\s\+\%#\@<!$\| \+\ze\t\|[^\t]\zs\t\+/

" Expand
imap <expr> <C-j>   vsnip#expandable()  ? '<Plug>(vsnip-expand)'         : '<C-j>'
smap <expr> <C-j>   vsnip#expandable()  ? '<Plug>(vsnip-expand)'         : '<C-j>'

" Expand or jump
imap <expr> <C-l>   vsnip#available(1)  ? '<Plug>(vsnip-expand-or-jump)' : '<C-l>'
smap <expr> <C-l>   vsnip#available(1)  ? '<Plug>(vsnip-expand-or-jump)' : '<C-l>'

" Jump forward or backward
imap <expr> <Tab>   vsnip#jumpable(1)   ? '<Plug>(vsnip-jump-next)'      : '<Tab>'
smap <expr> <Tab>   vsnip#jumpable(1)   ? '<Plug>(vsnip-jump-next)'      : '<Tab>'
imap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'
smap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'
