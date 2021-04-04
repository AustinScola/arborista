"""Test aborista.nodes.python.equals."""
from typing import Any

import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.equals import Equals


def test_inheritance() -> None:
    """Test aborista.nodes.python.equals.Equals inheritance."""
    assert issubclass(Equals, ComparisonOperator)


# yapf: disable
@pytest.mark.parametrize('equals, other, expected_equality', [
    (Equals(), 'foo', False),
    (Equals(), Equals(), True),
])
# yapf: enable
def test_eq(equals: Equals, other: Any, expected_equality: bool) -> None:
    """Test aborista.nodes.python.equals.Equals.__eq__."""
    equality: bool = equals == other

    assert equality == expected_equality
