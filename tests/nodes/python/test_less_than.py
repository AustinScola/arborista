"""Test aborista.nodes.python.less_than."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.less_than import LessThan


def test_inheritance() -> None:
    """Test aborista.nodes.python.less_than.LessThan inheritance."""
    assert issubclass(LessThan, ComparisonOperator)
