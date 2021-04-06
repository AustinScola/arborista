"""Test aborista.nodes.python.not_in."""
from typing import Any

import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.not_in import NotIn


def test_inheritance() -> None:
    """Test aborista.nodes.python.not_in.NotIn inheritance."""
    assert issubclass(NotIn, ComparisonOperator)


# yapf: disable
@pytest.mark.parametrize('not_in, other, expected_equality', [
    (NotIn(), 'foo', False),
    (NotIn(), NotIn(), True),
])
# yapf: enable
def test_eq(not_in: NotIn, other: Any, expected_equality: bool) -> None:
    """Test aborista.nodes.python.not_in.NotIn.__eq__."""
    equality: bool = not_in == other

    assert equality == expected_equality
