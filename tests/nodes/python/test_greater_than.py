"""Test aborista.nodes.python.greater_than."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.greater_than import GreaterThan


def test_inheritance() -> None:
    """Test aborista.nodes.python.greater_than.GreaterThan inheritance."""
    assert issubclass(GreaterThan, ComparisonOperator)
