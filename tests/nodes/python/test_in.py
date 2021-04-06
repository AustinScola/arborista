"""Test aborista.nodes.python.in_."""
from typing import Any

import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.in_ import In


def test_inheritance() -> None:
    """Test aborista.nodes.python.in_.In inheritance."""
    assert issubclass(In, ComparisonOperator)


# yapf: disable
@pytest.mark.parametrize('in_, other, expected_equality', [
    (In(), 'foo', False),
    (In(), In(), True),
])
# yapf: enable
def test_eq(in_: In, other: Any, expected_equality: bool) -> None:
    """Test aborista.nodes.python.in_.In.__eq__."""
    equality: bool = in_ == other

    assert equality == expected_equality
