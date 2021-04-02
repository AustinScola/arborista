"""Test aborista.nodes.python.less_than."""
from typing import Any

import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.less_than import LessThan


def test_inheritance() -> None:
    """Test aborista.nodes.python.less_than.LessThan inheritance."""
    assert issubclass(LessThan, ComparisonOperator)


# yapf: disable
@pytest.mark.parametrize('less_than, other, expected_equality', [
    (LessThan(), 'foo', False),
    (LessThan(), LessThan(), True),
])
# yapf: enable
def test_eq(less_than: LessThan, other: Any, expected_equality: bool) -> None:
    """Test aborista.nodes.python.less_than.LessThan.__eq__."""
    equality: bool = less_than == other

    assert equality == expected_equality
