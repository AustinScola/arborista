"""Test arborista.nodes.python.long_string."""
from arborista.nodes.python.long_string import LongString
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.long_string.LongString inheritance."""
    assert issubclass(LongString, PythonNode)
