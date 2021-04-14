"""Test arborista.nodes.python.ellipsis_node."""
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.ellipsis_node import EllipsisNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.ellipsis_node.EllipsisNode inheritance."""
    assert issubclass(EllipsisNode, Atom)
