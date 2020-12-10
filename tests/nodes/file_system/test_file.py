"""Test arborista.nodes.file_system.file."""
from pathlib import Path
from typing import Any

import pytest

from arborista.node import Node
from arborista.nodes.file_system.file import File


def test_inheritance() -> None:
    """Test arborista.nodes.file_system.file.File inheritance."""
    assert issubclass(File, Node)


# yapf: disable
@pytest.mark.parametrize('path, contents, expected_path, expected_contents', [
    (Path('foo'), '', Path('foo'), ''),
    (Path('foo'), 'bar', Path('foo'), 'bar'),
    (Path('foo/bar'), 'baz', Path('foo/bar'), 'baz'),
])
# yapf: enable
def test_init(path: Path, contents: str, expected_path: Path, expected_contents: str) -> None:
    """Test arborista.nodes.file_system.file.File.__init__."""
    file_: File = File(path, contents)

    assert file_.path == expected_path
    assert file_.contents == expected_contents


# yapf: disable
@pytest.mark.parametrize('file_, other, expected_equality', [
    (File(Path('foo'), ''), 'bar', False),
    (File(Path('foo'), 'bar'), File(Path('baz'), 'bar'), False),
    (File(Path('foo'), 'bar'), File(Path('foo'), 'baz'), False),
    (File(Path('foo'), 'bar'), File(Path('foo'), 'bar'), True),
    (File(Path('foo'), 'bar'), File(Path('foo/../foo'), 'bar'), True),
    (File(Path('foo/../foo'), 'bar'), File(Path('foo'), 'bar'), True),
])
# yapf: enable
def test_eq(file_: File, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.file_system.file.File.__eq__."""
    equality: bool = file_ == other
    assert equality == expected_equality
