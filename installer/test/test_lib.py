from installer import lib as lib


class TestUpdateDotfileRegion:
    def test_adds_region_at_top_of_empty_file(self):
        string = ""
        new_content = "Some\nMultiline\nstring"

        new_string = lib._update_dotfile_region(string, new_content, "#")

        expected_content = f"# {lib.REGION_START}\n{new_content}\n# {lib.REGION_END}\n"
        assert new_string == expected_content

    def test_adds_region_if_not_already_present(self):
        string = "Some text we want to keep here...\nSome more test to keep...\n"
        new_content = "Some\nMultiline\nstring"

        new_string = lib._update_dotfile_region(string, new_content, "//")

        expected_content = (
            "Some text we want to keep here...\n"
            "Some more test to keep...\n"
            "\n"
            f"// {lib.REGION_START}\n"
            f"{new_content}\n"
            f"// {lib.REGION_END}\n"
        )
        assert new_string == expected_content

    def test_replaces_old_content_with_new(self):
        string = (
            "Some text we want to keep here...\n"
            "Some more test to keep...\n"
            f"#{lib.REGION_START}\n"
            "To be replaced\n"
            f"#    {lib.REGION_END}\n"
            "This should also remain.\n"
        )
        new_content = "Some\nMultiline\nstring\n"

        new_string = lib._update_dotfile_region(string, new_content, "#")

        expected_content = (
            "Some text we want to keep here...\n"
            "Some more test to keep...\n"
            f"# {lib.REGION_START}\n"
            f"{new_content}"
            f"# {lib.REGION_END}\n"
            "This should also remain.\n"
        )
        assert new_string == expected_content
