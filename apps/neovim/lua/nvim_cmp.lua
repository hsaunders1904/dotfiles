-- Setup nvim-cmp.
local lspkind = require "lspkind"
local cmp = require "cmp"
local cmp_autopairs = require('nvim-autopairs.completion.cmp')

lspkind.init()

-- Add more filetypes for which to disable autocomplete here.
-- Can see filetype name using :lua print(vim.bo.filetype)
local disabled_filetypes = {
  "bib",
  "markdown",
  "neo-tree-popup",
  "plaintex",
  "rst",
  "tex",
  "text"
}

local function contains(list, x)
	for _, v in pairs(list) do
		if v == x then return true end
	end
	return false
end

cmp.setup({
  snippet = {
    -- REQUIRED - you must specify a snippet engine
    expand = function(args)
      vim.fn["vsnip#anonymous"](args.body) -- For `vsnip` users.
      -- require('luasnip').lsp_expand(args.body) -- For `luasnip` users.
      -- vim.fn["UltiSnips#Anon"](args.body) -- For `ultisnips` users.
      -- require'snippy'.expand_snippet(args.body) -- For `snippy` users.
    end,
  },
  mapping = {
    ["<C-n>"] = cmp.mapping.select_next_item { behavior = cmp.SelectBehavior.Insert },
    ["<C-p>"] = cmp.mapping.select_prev_item { behavior = cmp.SelectBehavior.Insert },
    ['<C-d>'] = cmp.mapping(cmp.mapping.scroll_docs(-4), { 'i', 'c' }),
    ['<C-f>'] = cmp.mapping(cmp.mapping.scroll_docs(4), { 'i', 'c' }),
    ['<C-Space>'] = cmp.mapping(cmp.mapping.complete(), { 'i', 'c' }),
    ['<C-y>'] = cmp.config.disable, -- Specify `cmp.config.disable` if you want to remove the default `<C-y>` mapping.
    ['<C-e>'] = cmp.mapping({
      i = cmp.mapping.abort(),
      c = cmp.mapping.close(),
    }),
    ['<CR>'] = cmp.mapping.confirm({ select = false }),
  },
  sources = cmp.config.sources({
    { name = 'nvim_lsp' },
    { name = "nvim_lua"},
    { name = "path"},
    { name = 'vsnip' }, -- For vsnip users.
    -- { name = 'luasnip' }, -- For luasnip users.
    -- { name = 'ultisnips' }, -- For ultisnips users.
    -- { name = 'snippy' }, -- For snippy users.
    { name = 'buffer', keyword_length = 5},
  }),
  formatting = {
    fields = {"kind", "abbr", "menu"},
    format = lspkind.cmp_format({
      mode = 'symbol',
      menu = {
	buffer = "[buf]",
	nvim_lsp = "[LSP]",
	nvim_lua = "[api]",
	path = "[path]",
	vsnip = "[snip]",
      }
    })
  },
  experimental = {
    native_menu = false,
    ghost_text = true,
  },
  window = {
    completion = {
      border = 'rounded',
      scrollbar = '║'
    },
    documentation = {
      border = 'rounded',
      scrollbar = '║'
    },
  },
})

-- Use buffer source for `/` (if you enabled `native_menu`, this won't work anymore).
cmp.setup.cmdline('/', {
  sources = {
    { name = 'buffer' }
  }
})

-- Use cmdline & path source for ':' (if you enabled `native_menu`, this won't work anymore).
cmp.setup.cmdline(':', {
  sources = cmp.config.sources({
    { name = 'path' }
  },
  {
    { name = 'cmdline' }
  })
})

cmp.event:on( 'confirm_done', cmp_autopairs.on_confirm_done({  map_char = { tex = '' } }))
