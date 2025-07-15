from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

from installer.base import Installer


class DummyInstaller(Installer):
    def install(self) -> bool:
        return True


@pytest.fixture
def installer():
    return DummyInstaller()


def test_repo_root_and_external_dir(installer):
    root = installer.repo_root()
    external = installer.external_dir()

    assert isinstance(root, Path)
    assert external == root / "external"


@patch("installer.base._read_file_if_exists")
@patch("installer.base.Path.open", new_callable=mock_open)
def test_update_dotfile_existing_file(mock_open_, mock_read, installer):
    mock_read.return_value = "\n".join(
        [
            installer.REGION_START,
            "old",
            installer.REGION_END,
        ]
    )
    path = Path("/fake/path")

    result = installer.update_dotfile(path, "new content", "#")

    assert result
    mock_open_.assert_called_once_with("w")
    handle = mock_open_()
    written_content = "".join(c[0][0] for c in handle.write.call_args_list)
    assert "new content" in written_content


@patch("installer.base._read_file_if_exists", return_value=None)
def test_update_dotfile_file_not_exists(mock_read, installer):
    path = Path("/does/not/exist")

    result = installer.update_dotfile(path, "new content", "#")

    assert result is False


@patch("subprocess.run")
def test_run_command_success(mock_run, installer):
    mock_run.return_value.returncode = 0

    result = installer.run_command(["echo", "hello"])

    assert result
    mock_run.assert_called_once()


def test_run_command_dry_run(installer):
    installer.dry_run = True

    result = installer.run_command(["echo", "hello"])

    assert result


@patch("subprocess.run")
def test_run_command_get_output(mock_run, installer):
    mock_run.return_value.stdout = b"output\n"

    result = installer.run_command_get_output(["echo", "hello"])

    assert result == "output\n"
    mock_run.assert_called_once()


def test_run_command_get_output_dry_run(installer):
    installer.dry_run = True

    result = installer.run_command_get_output(["echo", "hello"])

    assert result == ""


@patch("installer.base._download")
@patch("pathlib.Path.is_file", return_value=False)
def test_download_file_success(mock_is_file, mock_download, installer):
    url = "http://example.com/file"
    out_path = Path("/tmp/file")

    result = installer.download_file(url, out_path)

    assert result
    mock_download.assert_called_once_with(url, out_path)


@patch("pathlib.Path.is_file", return_value=True)
def test_download_file_exists_no_force(mock_is_file, installer):
    url = "http://example.com/file"
    out_path = Path("/tmp/file")

    result = installer.download_file(url, out_path)

    assert result is False


@patch("installer.base._download", side_effect=Exception("fail"))
@patch("pathlib.Path.is_file", return_value=False)
def test_download_file_failure(mock_is_file, mock_download, installer):
    url = "http://example.com/file"
    out_path = Path("/tmp/file")

    result = installer.download_file(url, out_path)

    assert result is False


@patch("installer.base.Installer.run_command", return_value=True)
@patch("pathlib.Path.is_file", return_value=False)
def test_make_symlink_success(mock_is_file, mock_run, installer):
    origin = Path("/origin")
    link = Path("/link")

    result = installer.make_symlink(origin, link)

    assert result
    mock_run.assert_called_once()


@patch("pathlib.Path.is_file", return_value=True)
def test_make_symlink_link_exists(mock_is_file, installer):
    origin = Path("/origin")
    link = Path("/link")

    result = installer.make_symlink(origin, link)

    assert result is False
