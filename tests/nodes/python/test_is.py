"""Test aborista.nodes.python.is_."""
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.is_ import Is


def test_inheritance() -> None:
    """Test aborista.nodes.python.is_.Is inheritance."""
    assert issubclass(Is, ComparisonOperator)
