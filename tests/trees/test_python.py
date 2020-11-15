"""Test arborista.trees.python."""
from arborista.tree import Tree
from arborista.trees.python import Python


def test_inheritance() -> None:
    """Test arborista.trees.python.Python inheritance."""
    assert issubclass(Python, Tree)
