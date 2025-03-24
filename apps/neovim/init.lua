local dotfiles_dir = os.getenv('DOTFILES_DIR')

-- Load vanilla Vim config
vim.cmd('source ' .. dotfiles_dir .. '/dotfiles/.vimrc')
vim.opt.runtimepath:append(dotfiles_dir .. '/apps/neovim')

-- Add these dotfiles to the runtime path
local dotfiles_rt_path = dotfiles_dir .. '/apps/neovim/lua/?.lua'
package.path = package.path .. ';' .. dotfiles_rt_path

-- Plugins
require('config.lazy') -- must be imported first
require("mason").setup {}
require('telescope').setup {}
require('toggleterm').setup {}

-- Configs
require("config.cmp")
require('config.lsp')

-- Mappings
vim.api.nvim_set_keymap(
    'n',
    '<leader>tt',
    ':ToggleTerm<CR>',
    { noremap = true, silent = true }
)
vim.api.nvim_set_keymap(
    'n',
    '<leader>vs',
    ':vsplit<CR>',
    { noremap = true, silent = true }
)
vim.api.nvim_set_keymap(
    "n",
    "<leader>/",
    "gcc",
    { noremap = false, silent = true }
)
vim.api.nvim_set_keymap(
    "v",
    "<leader>/",
    "gc",
    { noremap = false, silent = true }
)
