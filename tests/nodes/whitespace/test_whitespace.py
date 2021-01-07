"""Test arborista.nodes.whitespace.whitespace."""
from arborista.node import Node
from arborista.nodes.whitespace.whitespace import Whitespace


def test_inheritance() -> None:
    """Test arborista.nodes.whitespace.whitespace.Whitespace inheritance."""
    assert issubclass(Whitespace, Node)
