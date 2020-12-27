"""Test arborista.nodes.file_system.path_node."""
from pathlib import Path
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node
from arborista.nodes.file_system.path_node import PathNode


def test_inheritance() -> None:
    """Test arborista.nodes.file_system.path_node.PathNode inheritance."""
    assert issubclass(PathNode, Node)


# yapf: disable
@pytest.mark.parametrize('path, parent, pass_parent, expected_parent', [
    (Path('foo.py'), None, False, None),
    (Path('foo.py'), None, True, None),
    (Path('foo.py'), PathNode(Path('foo.py')), True, PathNode(Path('foo.py'))),
])
# yapf: enable
def test_init(path: Path, parent: Optional[Node], pass_parent: bool,
              expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.file_system.path_node.PathNode.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    path_node: PathNode = PathNode(path, **keyword_arguments)

    assert path_node.path == path
    assert path_node.parent == expected_parent


# yapf: disable
@pytest.mark.parametrize('path_node, other, expected_equality', [
    (PathNode(Path('foo.py')), 'foo.py', False),
    (PathNode(Path('foo.py')), PathNode(Path('bar.py')), False),
    (PathNode(Path('foo.py')), PathNode(Path('foo.py')), True),
])
# yapf: enable
def test_eq(path_node: PathNode, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.file_system.path_node.PathNode.__eq__."""
    equality: bool = path_node == other

    assert equality == expected_equality
