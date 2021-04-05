"""Test aborista.nodes.python.greater_than_or_equals."""
from typing import Any

import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.greater_than_or_equals import GreaterThanOrEquals


def test_inheritance() -> None:
    """Test aborista.nodes.python.greater_than_or_equals.GreaterThanOrEquals inheritance."""
    assert issubclass(GreaterThanOrEquals, ComparisonOperator)


# yapf: disable
@pytest.mark.parametrize('greater_than_or_equals, other, expected_equality', [
    (GreaterThanOrEquals(), 'foo', False),
    (GreaterThanOrEquals(), GreaterThanOrEquals(), True),
])
# yapf: enable
def test_eq(greater_than_or_equals: GreaterThanOrEquals, other: Any,
            expected_equality: bool) -> None:
    """Test aborista.nodes.python.greater_than_or_equals.GreaterThanOrEquals.__eq__."""
    equality: bool = greater_than_or_equals == other

    assert equality == expected_equality
