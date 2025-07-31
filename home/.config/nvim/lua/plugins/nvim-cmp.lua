return {
    "hrsh7th/nvim-cmp",
    event = "InsertEnter",
    dependencies = {
        "hrsh7th/cmp-nvim-lsp",      -- LSP source
        "hrsh7th/cmp-buffer",        -- Buffer source
        "hrsh7th/cmp-path",          -- File path completions
        "hrsh7th/cmp-cmdline",       -- Command-line completions
        "L3MON4D3/LuaSnip",          -- Snippet engine
        "saadparwaiz1/cmp_luasnip",  -- Snippet completions
        "rafamadriz/friendly-snippets" -- Preconfigured snippets
    }
}
