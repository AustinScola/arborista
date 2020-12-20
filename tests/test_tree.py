"""Test arborista.tree."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node
from arborista.nodes.python.module import Module
from arborista.tree import Tree
from tests.animal_nodes import Dog


# yapf: disable
@pytest.mark.parametrize('root, pass_root, expected_root', [
    (None, False, None),
    (None, True, None),
    (Dog(), True, Dog()),
])
# yapf: enable
def test_init(root: Optional[Node], pass_root: bool, expected_root: Optional[Node]) -> None:
    """Test arborista.tree.Tree.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_root:
        keyword_arguments['root'] = root

    tree: Tree = Tree(**keyword_arguments)

    assert tree.root == expected_root


# yapf: disable
@pytest.mark.parametrize('tree, other, expected_equality', [
    (Tree(root=None), 'foo', False),
    (Tree(root=None), Tree(root=Module('foo')), False),
    (Tree(root=Module('foo')), Tree(root=Module('bar')), False),
    (Tree(root=None), Tree(root=None), True),
    (Tree(root=Module('foo')), Tree(root=Module('foo')), True),
])
# yapf: enable
def test_tree_eq(tree: Tree, other: Any, expected_equality: bool) -> None:
    """Test arborista.tree.Tree.__eq__."""
    equality: bool = tree == other
    assert equality == expected_equality
