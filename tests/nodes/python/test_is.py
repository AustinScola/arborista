"""Test aborista.nodes.python.is_."""
from typing import Any

import pytest

from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.is_ import Is


def test_inheritance() -> None:
    """Test aborista.nodes.python.is_.Is inheritance."""
    assert issubclass(Is, ComparisonOperator)


# yapf: disable
@pytest.mark.parametrize('is_, other, expected_equality', [
    (Is(), 'foo', False),
    (Is(), Is(), True),
])
# yapf: enable
def test_eq(is_: Is, other: Any, expected_equality: bool) -> None:
    """Test aborista.nodes.python.is_.Is.__eq__."""
    equality: bool = is_ == other

    assert equality == expected_equality
