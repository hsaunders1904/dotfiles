local dotfiles_dir = os.getenv('DOTFILES_DIR')

-- Load vanilla Vim config
vim.cmd('source ' .. dotfiles_dir .. '/home/.vimrc')
vim.opt.runtimepath:append(dotfiles_dir .. '/home/.config/nvim')

-- Add these dotfiles to the runtime path
local dotfiles_rt_path = dotfiles_dir .. '/home/.config/nvim/lua/?.lua'
package.path = package.path .. ';' .. dotfiles_rt_path

-- Plugins
require('config.lazy') -- must be imported first
require("mason").setup {}
require('telescope').setup {}
require('toggleterm').setup {}

-- Configs
require("config.cmp")
require('config.lsp')
require('config.vertical-bars')

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

-- Send all deletes to 'd' register, so system clipboard is not clobbered
vim.opt.clipboard = ""
vim.keymap.set({ 'n', 'x' }, 'd', '"dd', { noremap = true })
vim.keymap.set({ 'n', 'x' }, 'c', '"dc', { noremap = true })
vim.keymap.set('n', 'D', '"dD', { noremap = true })
vim.keymap.set('n', 'C', '"dC', { noremap = true })
vim.keymap.set('n', 'x', '"dx', { noremap = true })
vim.keymap.set('x', 'x', '"dx', { noremap = true })
-- Make `y` yank to system clipboard if no register given
vim.keymap.set({ 'n', 'x' }, 'y', function()
    if vim.v.register == '"' then
        return '"+y'
    else
        return 'y'
    end
end, { expr = true, noremap = true })
