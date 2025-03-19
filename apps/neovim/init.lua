function file_exists(name)
    local f = io.open(name,"r")
    if f ~= nil then io.close(f) return true else return false end
end

dotfiles_dir = os.getenv('DOTFILES_DIR')
vimrc =  dotfiles_dir .. '/dotfiles/.vimrc'
if file_exists(vimrc) then
    vim.cmd('source' .. vimrc)
end

vim.g.mapleader = " "
vim.g.maplocalleader = "\\"

vim.opt.runtimepath:append(dotfiles_dir .. '/apps/neovim')
require("config.lazy")
require("telescope").setup()


-- require "user.alpha"
-- require "user.autocommands"
-- require "user.autopairs"
-- require "user.bufferline"
-- require "user.cmp"
-- require "user.colorscheme"
-- require "user.comment"
-- require "user.gitsigns"
-- require "user.impatient"
-- require "user.indentline"
-- require "user.keymaps"
-- require "user.lualine"
-- require "user.nvim-tree"
-- require "user.options"
-- require "user.plugins"
-- require "user.project"
-- require "user.telescope"
-- require "user.toggleterm"
-- require "user.treesitter"
-- require "user.whichkey"
