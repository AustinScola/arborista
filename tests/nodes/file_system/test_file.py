"""Test arborista.nodes.file_system.file."""
from pathlib import Path
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node
from arborista.nodes.file_system.file import File


def test_inheritance() -> None:
    """Test arborista.nodes.file_system.file.File inheritance."""
    assert issubclass(File, Node)


# yapf: disable
@pytest.mark.parametrize('path, contents, parent, pass_parent, expected_path, expected_contents', [
    (Path('foo'), '', None, False, Path('foo'), ''),
    (Path('foo'), '', None, True, Path('foo'), ''),
    (Path('foo'), 'bar', None, False, Path('foo'), 'bar'),
    (Path('foo'), 'bar', None, True, Path('foo'), 'bar'),
    (Path('foo/bar'), 'baz', None, False, Path('foo/bar'), 'baz'),
    (Path('foo/bar'), 'baz', None, True, Path('foo/bar'), 'baz'),
])
# yapf: enable
# pylint: disable=too-many-arguments
def test_init(path: Path, contents: str, parent: Optional[Node], pass_parent: bool,
              expected_path: Path, expected_contents: str) -> None:
    """Test arborista.nodes.file_system.file.File.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    file_: File = File(path, contents, **keyword_arguments)

    assert file_.path == expected_path
    assert file_.contents == expected_contents
    assert id(file_.parent) == id(parent)


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


# yapf: disable
@pytest.mark.parametrize('file_, expected_stem', [
    (File(Path('foo'), ''), 'foo'),
    (File(Path('foo.py'), ''), 'foo'),
    (File(Path('foo/bar'), ''), 'bar'),
    (File(Path('foo/bar.py'), ''), 'bar'),
])
# yapf: enable
def test_stem(file_: File, expected_stem: str) -> None:
    """Test arborista.nodes.file_system.file.File.stem."""
    assert file_.stem == expected_stem
