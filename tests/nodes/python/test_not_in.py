"""Test aborista.nodes.python.not_in."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.not_in import NotIn


def test_inheritance() -> None:
    """Test aborista.nodes.python.not_in.NotIn inheritance."""
    assert issubclass(NotIn, ComparisonOperator)
