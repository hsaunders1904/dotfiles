require("mason-lspconfig").setup({
    ensure_installed = { "pyright" }
})

local lspconfig = require("lspconfig")
lspconfig.pyright.setup({
    capabilities = require("cmp_nvim_lsp").default_capabilities(),
    settings = {
        python = {
            analysis = {
                typeCheckingMode = "strict",
                autoImportCompletions = true,
                useLibraryCodeForTypes = true,
            },
        },
    },
})
