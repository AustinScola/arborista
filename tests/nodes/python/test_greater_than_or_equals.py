"""Test aborista.nodes.python.greater_than_or_equals."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.greater_than_or_equals import GreaterThanOrEquals


def test_inheritance() -> None:
    """Test aborista.nodes.python.greater_than_or_equals.GreaterThanOrEquals inheritance."""
    assert issubclass(GreaterThanOrEquals, ComparisonOperator)
