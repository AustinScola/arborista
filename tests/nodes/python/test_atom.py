"""Test arborista.nodes.python.atom."""
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.atom.Atom inheritance."""
    assert issubclass(Atom, PythonNode)
