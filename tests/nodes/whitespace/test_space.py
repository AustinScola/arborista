"""Test arborista.nodes.whitespace.space."""
from typing import Any

import pytest

from arborista.nodes.whitespace.space import Space
from arborista.nodes.whitespace.whitespace import Whitespace


def test_inheritance() -> None:
    """Test arborista.nodes.whitespace.space.Space inheritance."""
    assert issubclass(Space, Whitespace)


# yapf: disable
@pytest.mark.parametrize('space, other, expected_equality', [
    (Space(), 'foo', False),
    (Space(), Space(), True),
])
# yapf: enable
def test_eq(space: Space, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.whitespace.space.Space.__eq__."""
    equality: bool = space == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('space, expected_string', [
    (Space(), ' '),
])
# yapf: enable
def test_str(space: Space, expected_string: str) -> None:
    """Test arborista.nodes.whitespace.space.Space.__str__."""
    string: str = str(space)

    assert string == expected_string
