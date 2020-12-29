"""Test arborista.nodes.python.number."""
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.number import Number


def test_inheritance() -> None:
    """Test arborista.nodes.python.number.Number inheritance."""
    assert issubclass(Number, Atom)
