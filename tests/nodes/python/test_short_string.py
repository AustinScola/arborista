"""Test arborista.nodes.python.short_string."""
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.short_string import ShortString


def test_inheritance() -> None:
    """Test arborista.nodes.python.short_string.ShortString inheritance."""
    assert issubclass(ShortString, PythonNode)
