"""Test aborista.nodes.python.less_greater_than."""
from typing import Any

import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.less_greater_than import LessGreaterThan


def test_inheritance() -> None:
    """Test aborista.nodes.python.less_greater_than.LessGreaterThan inheritance."""
    assert issubclass(LessGreaterThan, ComparisonOperator)


# yapf: disable
@pytest.mark.parametrize('less_greater_than, other, expected_equality', [
    (LessGreaterThan(), 'foo', False),
    (LessGreaterThan(), LessGreaterThan(), True),
])
# yapf: enable
def test_eq(less_greater_than: LessGreaterThan, other: Any, expected_equality: bool) -> None:
    """Test aborista.nodes.python.less_greater_than.LessGreaterThan.__eq__."""
    equality: bool = less_greater_than == other

    assert equality == expected_equality
