set nocompatible
filetype off

source ${DOTFILES_DIR}/external/plug.vim
call plug#begin()
 " General requirement:q!s
 Plug 'nvim-lua/plenary.nvim'
 Plug 'kyazdani42/nvim-web-devicons'
 Plug 'MunifTanjim/nui.nvim'

 " Language server and highlighting
 Plug 'neovim/nvim-lspconfig'
 Plug 'nvim-treesitter/nvim-treesitter'
 Plug 'nvim-treesitter/nvim-treesitter-context'
 Plug 'nvim-treesitter/playground'

 " Telescope for searching
 Plug 'nvim-telescope/telescope.nvim', {'tag': '0.1.x'}
 Plug 'nvim-telescope/telescope-fzf-native.nvim', { 'do': 'make' }

 " Sleuth to set indent options
 Plug 'tpope/vim-sleuth'

 " Big git plugin
 Plug 'tpope/vim-fugitive'
 Plug 'lewis6991/gitsigns.nvim'
 Plug 'sindrets/diffview.nvim'
 Plug 'numToStr/Comment.nvim'
 Plug 'nvim-lualine/lualine.nvim'
 Plug 'ellisonleao/gruvbox.nvim'

 " nvim-cmp config for autocomplete
 Plug 'hrsh7th/nvim-cmp'
 Plug 'hrsh7th/cmp-buffer'
 Plug 'hrsh7th/cmp-path'
 Plug 'hrsh7th/cmp-nvim-lua'
 Plug 'hrsh7th/cmp-nvim-lsp'
 Plug 'hrsh7th/cmp-cmdline'

 " Spinner for lsp progress
 Plug 'j-hui/fidget.nvim'

 " lots of snippets for vsnip
 Plug 'rafamadriz/friendly-snippets'

 " lspkind for formatting
 Plug 'onsails/lspkind.nvim'

 " For vsnip users.
 Plug 'hrsh7th/cmp-vsnip'
 Plug 'hrsh7th/vim-vsnip'

 " Function signature help
 Plug 'ray-x/lsp_signature.nvim'

 " autopairs
 Plug 'windwp/nvim-autopairs'

 " Replace arguements etc
 Plug 'wellle/targets.vim'

 " Read/write files with sudo:
 Plug 'lambdalisue/suda.vim'

 " Side bar based, function name and jumping based on tree-sitter
 Plug 'stevearc/aerial.nvim'

 " Filesystem tree
 Plug 'nvim-neo-tree/neo-tree.nvim'

 " Toggleable terminal
 Plug 'akinsho/toggleterm.nvim'

 " Pretty diagnostic list
 Plug 'folke/trouble.nvim'
 " Navigating quickfix lists
 Plug 'tpope/vim-unimpaired'

 " Better searching (visual line asterisk)
 Plug 'haya14busa/vim-asterisk'
call plug#end()

if !empty('$DOTFILES_DIR')
  " Add the directory to the runtime path
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

set foldmethod=expr
set foldexpr=nvim_treesitter#foldexpr()
set foldlevel=20

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

" Fuigitive:
nmap <leader>gj :diffget //3<CR>
nmap <leader>gf :diffget //2<CR>
nmap <leader>gs :G<CR>
set diffopt+=vertical

lua require("telescope_maps")

" Open Neotree
nmap <Leader>t :Neotree toggle<CR>
let g:neo_tree_remove_legacy_commands = 1

" NOTE: You can use other key to expand snippet.

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

" Select or cut text to use as $TM_SELECTED_TEXT in the next snippet.
" See https://github.com/hrsh7th/vim-vsnip/pull/50
"nmap        s   <Plug>(vsnip-select-text)
"xmap        s   <Plug>(vsnip-select-text)
"nmap        S   <Plug>(vsnip-cut-text)
"xmap        S   <Plug>(vsnip-cut-text)

" Ctrl-w to exit terminal mode
tnoremap <C-w> <C-\><C-n>
" Send line to toggleterm using vim slime binding
" use n<c-c><c-c> to send to terminal n
xnoremap <c-c><c-c> :<C-u>exe "ToggleTermSendVisualSelection" . v:count1<CR>
nnoremap <c-c><c-c> :<C-u>exe "ToggleTermSendCurrentLine" . v:count1<CR>

" Copy line for debugger
nnoremap <silent> \p :execute "let @+='".expand('%:p').":".getpos('.')[1]."'"<cr>:echo "Location copied"<cr>

" vim-asterisk mappings
map *   <Plug>(asterisk-*)
map #   <Plug>(asterisk-#)
map g*  <Plug>(asterisk-g*)
map g#  <Plug>(asterisk-g#)
map z*  <Plug>(asterisk-z*)
map gz* <Plug>(asterisk-gz*)
map z#  <Plug>(asterisk-z#)
map gz# <Plug>(asterisk-gz#)

" LSP config for goto/references etc
lua require("aerial_config")
lua require('lsp_signature').setup()
lua require("fidget").setup{}
lua require("nvim_cmp")
lua require('nvim-autopairs').setup{}
lua require("nvim_treesitter_config")
lua require('treesitter-context').setup{}
lua require("lsp_config")
lua require("nvim_treesitter_playground_config")
lua require("Comment").setup()
lua require("lualine_config")
lua require("toggleterm").setup{open_mapping="<C-x>"}
lua require("diffview_config")
lua require('gitsigns').setup()
lua require("telescope").setup({defaults = { mappings = { i = { ["<C-e>"] = { "<esc>", type = "command" }, ['<esc>'] = require("telescope.actions").close }, }, }, })
lua require('telescope').load_extension('fzf')

lua require('trouble_maps')
