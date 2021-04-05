"""Test aborista.nodes.python.less_than_or_equals."""
from typing import Any

import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.less_than_or_equals import LessThanOrEquals


def test_inheritance() -> None:
    """Test aborista.nodes.python.less_than_or_equals.LessThanOrEquals inheritance."""
    assert issubclass(LessThanOrEquals, ComparisonOperator)


# yapf: disable
@pytest.mark.parametrize('less_than_or_equals, other, expected_equality', [
    (LessThanOrEquals(), 'foo', False),
    (LessThanOrEquals(), LessThanOrEquals(), True),
])
# yapf: enable
def test_eq(less_than_or_equals: LessThanOrEquals, other: Any, expected_equality: bool) -> None:
    """Test aborista.nodes.python.less_than_or_equals.LessThanOrEquals.__eq__."""
    equality: bool = less_than_or_equals == other

    assert equality == expected_equality
