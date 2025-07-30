require("mason-lspconfig").setup({
    ensure_installed = { "clangd" }
})

local lspconfig = require("lspconfig")
lspconfig.clangd.setup({
    cmd = { "clangd", "--background-index" },
    root_dir = lspconfig.util.root_pattern("compile_commands.json", ".git")}
)
