"""Test arborista.tree."""
from arborista.node import Node
from arborista.tree import Tree


def test_init() -> None:
    """Test arborista.tree.Tree.__init__"""
    root: Node = Node()
    tree: Tree = Tree(root)
    assert tree.root == root
