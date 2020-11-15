"""Test arborista.nodes.python.python_node."""
from arborista.node import Node
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.python_node.PythonNode inheritance."""
    assert issubclass(PythonNode, Node)
