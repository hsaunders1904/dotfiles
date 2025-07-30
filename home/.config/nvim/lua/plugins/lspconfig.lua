return {
    "neovim/nvim-lspconfig",
    event = { "BufReadPre", "BufNewFile" },
    dependencies = {
        { "williamboman/mason.nvim",          config = true },
        { "williamboman/mason-lspconfig.nvim" },
    }
}
