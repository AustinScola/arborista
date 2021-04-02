"""Test arborista.nodes.python.comparison_operator."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.comparison_operator.ComparisonOperator inheritance."""
    assert issubclass(ComparisonOperator, PythonNode)
