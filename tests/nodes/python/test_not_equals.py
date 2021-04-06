"""Test aborista.nodes.python.not_equals."""
from typing import Any

import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.not_equals import NotEquals


def test_inheritance() -> None:
    """Test aborista.nodes.python.not_equals.NotEquals inheritance."""
    assert issubclass(NotEquals, ComparisonOperator)


# yapf: disable
@pytest.mark.parametrize('not_equals, other, expected_equality', [
    (NotEquals(), 'foo', False),
    (NotEquals(), NotEquals(), True),
])
# yapf: enable
def test_eq(not_equals: NotEquals, other: Any, expected_equality: bool) -> None:
    """Test aborista.nodes.python.not_equals.NotEquals.__eq__."""
    equality: bool = not_equals == other

    assert equality == expected_equality
