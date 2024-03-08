local actions = require("diffview.actions")
require("diffview").setup({
  view = {
    merge_tool = {
      -- Config for conflicted files in diff views during a merge or rebase.
      layout = "diff3_mixed",
    },
  },
})
