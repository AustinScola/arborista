"""Test aborista.nodes.python.not_equals."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.not_equals import NotEquals


def test_inheritance() -> None:
    """Test aborista.nodes.python.not_equals.NotEquals inheritance."""
    assert issubclass(NotEquals, ComparisonOperator)
