"""Test aborista.nodes.python.is_not."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.is_not import IsNot


def test_inheritance() -> None:
    """Test aborista.nodes.python.is_not.IsNot inheritance."""
    assert issubclass(IsNot, ComparisonOperator)
