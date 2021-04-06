"""Test aborista.nodes.python.is_not."""
from typing import Any

import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.is_not import IsNot


def test_inheritance() -> None:
    """Test aborista.nodes.python.is_not.IsNot inheritance."""
    assert issubclass(IsNot, ComparisonOperator)


# yapf: disable
@pytest.mark.parametrize('is_not, other, expected_equality', [
    (IsNot(), 'foo', False),
    (IsNot(), IsNot(), True),
])
# yapf: enable
def test_eq(is_not: IsNot, other: Any, expected_equality: bool) -> None:
    """Test aborista.nodes.python.is_not.IsNot.__eq__."""
    equality: bool = is_not == other

    assert equality == expected_equality
