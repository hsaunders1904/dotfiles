require("lualine").setup({
  sections = {
    lualine_x = { 'aerial' },
    lualine_y = {'encoding', 'fileformat', 'filetype'},
    lualine_z = {'progress', 'location'},
  },
  extensions = {'aerial', 'fugitive', 'fzf', 'neo-tree'},
  theme = "gruvbox_dark",
  options = {
    section_separators = '',
    component_separators = '',
  },
})
