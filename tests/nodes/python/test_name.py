"""Test arborista.nodes.python.name."""
from typing import Any

import pytest

from arborista.nodes.python.atom import Atom
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.nodes.python.name.Name inheritance."""
    assert issubclass(Name, Atom)


# yapf: disable
@pytest.mark.parametrize('value', [
    ('f'),
])
# yapf: enable
def test_init(value: str) -> None:
    """Test arborista.nodes.python.name.__init__."""
    name: Name = Name(value)

    assert name.value == value


# yapf: disable
@pytest.mark.parametrize('name, other, expected_equality', [
    (Name('foo'), 'bar', False),
    (Name('foo'), Name('foo'), True),
])
# yapf: enable
def test_eq(name: Name, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.name.__eq__."""
    equality: bool = name == other
    assert equality == expected_equality
