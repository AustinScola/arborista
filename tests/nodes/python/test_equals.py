"""Test aborista.nodes.python.equals."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.equals import Equals


def test_inheritance() -> None:
    """Test aborista.nodes.python.equals.Equals inheritance."""
    assert issubclass(Equals, ComparisonOperator)
