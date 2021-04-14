"""Test arborista.nodes.python.star."""
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.star import Star


def test_inheritance() -> None:
    """Test arborista.nodes.python.star.Star inheritance."""
    assert issubclass(Star, PythonNode)
