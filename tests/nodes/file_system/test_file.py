"""Test arborista.nodes.file_system.file."""
from pathlib import Path
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.file_system.file import File
from arborista.nodes.python.module import Module
from arborista.nodes.sequences.text.string import String


def test_inheritance() -> None:
    """Test arborista.nodes.file_system.file.File inheritance."""
    assert issubclass(File, Node)


# yapf: disable
@pytest.mark.parametrize('path, contents, parent, pass_parent, expected_path, expected_contents', [
    (Path('foo'), String(), None, False, Path('foo'), String()),
    (Path('foo'), String(), None, True, Path('foo'), String()),
    (Path('foo'), String('bar'), None, False, Path('foo'), String('bar')),
    (Path('foo'), String('bar'), None, True, Path('foo'), String('bar')),
    (Path('foo/bar'), String('baz'), None, False, Path('foo/bar'), String('baz')),
    (Path('foo/bar'), String('baz'), None, True, Path('foo/bar'), String('baz')),
])
# yapf: enable
# pylint: disable=too-many-arguments
def test_init(path: Path, contents: Node, parent: Optional[Node], pass_parent: bool,
              expected_path: Path, expected_contents: str) -> None:
    """Test arborista.nodes.file_system.file.File.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    file_: File = File(path, contents, **keyword_arguments)

    assert file_.path == expected_path
    assert file_.contents == expected_contents
    assert file_.parent is parent


# yapf: disable
@pytest.mark.parametrize('file_, other, expected_equality', [
    (File(Path('foo'), String()), 'bar', False),
    (File(Path('foo'), String('bar')), File(Path('baz'), String('bar')), False),
    (File(Path('foo'), String('bar')), File(Path('foo'), String('baz')), False),
    (File(Path('foo'), String('bar')), File(Path('foo'), String('bar')), True),
    (File(Path('foo'), String('bar')), File(Path('foo/../foo'), String('bar')), True),
    (File(Path('foo/../foo'), String('bar')), File(Path('foo'), String('bar')), True),
])
# yapf: enable
def test_eq(file_: File, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.file_system.file.File.__eq__."""
    equality: bool = file_ == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('file_, expected_children_list', [
    (File(Path('foo.py'), String()), [String()]),
    (File(Path('foo.py'), Module('foo', [])), [Module('foo', [])]),
])
# yapf: enable
def test_iterate_children(file_: File, expected_children_list: NodeList) -> None:
    """Test arborista.nodes.file_system.file.File.iterate_children."""
    children: NodeIterator = file_.iterate_children()
    children_list: NodeList = list(children)

    assert children_list == expected_children_list


# yapf: disable
@pytest.mark.parametrize('file_, expected_stem', [
    (File(Path('foo'), String()), 'foo'),
    (File(Path('foo.py'), String()), 'foo'),
    (File(Path('foo/bar'), String()), 'bar'),
    (File(Path('foo/bar.py'), String()), 'bar'),
])
# yapf: enable
def test_stem(file_: File, expected_stem: str) -> None:
    """Test arborista.nodes.file_system.file.File.stem."""
    assert file_.stem == expected_stem
