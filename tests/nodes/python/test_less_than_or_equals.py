"""Test aborista.nodes.python.less_than_or_equals."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.less_than_or_equals import LessThanOrEquals


def test_inheritance() -> None:
    """Test aborista.nodes.python.less_than_or_equals.LessThanOrEquals inheritance."""
    assert issubclass(LessThanOrEquals, ComparisonOperator)
