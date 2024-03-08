local builtin = require('telescope.builtin')
-- " Don't match filenames with ripgrep:
-- command! -bang -nargs=* Rg
--   \ call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case ".shellescape(<q-args>), 1,
--   \   fzf#vim#with_preview({'options': '--delimiter : --nth 4..'}), <bang>0)

local function recent_buffers() builtin.buffers({sort_mru=true, ignore_current_buffer=true}) end

vim.keymap.set('n', '<leader>ff', builtin.git_files, {})
vim.keymap.set('n', '<leader>fF', builtin.find_files, {})
vim.keymap.set('n', '<leader>fg', builtin.live_grep, {})
vim.keymap.set('n', '<leader>fb', recent_buffers, {})
vim.keymap.set('n', '<leader>fh', builtin.oldfiles, {})
vim.keymap.set('n', '<leader>fH', builtin.help_tags, {})
vim.keymap.set('n', '<leader>fl', builtin.current_buffer_fuzzy_find, {})
vim.keymap.set('n', '<leader>fC', builtin.commands, {})
vim.keymap.set('n', '<leader>f:', builtin.command_history, {})
vim.keymap.set('n', '<leader>fM', builtin.keymaps, {})

vim.keymap.set('n', '<leader>fs', builtin.lsp_document_symbols, {})
vim.keymap.set('n', '<leader>fS', builtin.lsp_workspace_symbols, {})
