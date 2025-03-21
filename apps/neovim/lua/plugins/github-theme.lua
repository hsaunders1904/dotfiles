return {
    'projekt0n/github-nvim-theme',
    tag = '1.1.2',
    name = 'github-theme',
    lazy = false,
    priority = 1000,
    config = function()
        require('github-theme').setup{}
        vim.cmd('colorscheme github_dark')
    end,
}
