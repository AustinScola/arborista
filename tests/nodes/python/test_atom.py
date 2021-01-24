"""Test arborista.nodes.python.atom."""
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.expression import Expression


def test_inheritance() -> None:
    """Test arborista.nodes.python.atom.Atom inheritance."""
    assert issubclass(Atom, Expression)
