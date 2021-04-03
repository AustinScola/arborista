"""Test aborista.nodes.python.greater_than."""
from typing import Any

import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.greater_than import GreaterThan


def test_inheritance() -> None:
    """Test aborista.nodes.python.greater_than.GreaterThan inheritance."""
    assert issubclass(GreaterThan, ComparisonOperator)


# yapf: disable
@pytest.mark.parametrize('greater_than, other, expected_equality', [
    (GreaterThan(), 'foo', False),
    (GreaterThan(), GreaterThan(), True),
])
# yapf: enable
def test_eq(greater_than: GreaterThan, other: Any, expected_equality: bool) -> None:
    """Test aborista.nodes.python.greater_than.GreaterThan.__eq__."""
    equality: bool = greater_than == other

    assert equality == expected_equality
