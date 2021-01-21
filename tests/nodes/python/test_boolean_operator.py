"""Test arborista.nodes.python.boolean_operator."""
from arborista.nodes.python.boolean_operator import BooleanOperator
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.boolean_operator.BooleanOperator inheritance."""
    assert issubclass(BooleanOperator, PythonNode)
