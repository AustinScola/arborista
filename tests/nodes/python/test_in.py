"""Test aborista.nodes.python.in_."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.in_ import In


def test_inheritance() -> None:
    """Test aborista.nodes.python.in_.In inheritance."""
    assert issubclass(In, ComparisonOperator)
