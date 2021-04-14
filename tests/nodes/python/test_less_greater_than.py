"""Test aborista.nodes.python.less_greater_than."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.less_greater_than import LessGreaterThan


def test_inheritance() -> None:
    """Test aborista.nodes.python.less_greater_than.LessGreaterThan inheritance."""
    assert issubclass(LessGreaterThan, ComparisonOperator)
