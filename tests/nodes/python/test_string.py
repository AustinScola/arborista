"""Test arborista.nodes.python.string."""
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.string import String


def test_inheritance() -> None:
    """Test arborista.nodes.python.string.String inheritance."""
    assert issubclass(String, Atom)
