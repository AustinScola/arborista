"""Test arborista.nodes.python.integer."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.number import Number
from testing_helpers.animal_nodes import Dog


def test_inheritance() -> None:
    """Test arborista.nodes.python.integer.Integer inheritance."""
    assert issubclass(Integer, Number)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent, expected_parent', [
    (0, None, False, None),
    (0, None, True, None),
    (0, Dog(), True, Dog()),
])
# yapf: enable
def test_init(value: int, parent: Optional[Node], pass_parent: bool,
              expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.integer.Integer.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    integer = Integer(value, **keyword_arguments)

    assert integer.value == value
    assert integer.parent == expected_parent


# yapf: disable
@pytest.mark.parametrize('integer, other, expected_equality', [
    (Integer(1), 'foo', False),
    (Integer(1), Integer(2), False),
    (Integer(1), Integer(1), True),
])
# yapf: enable
def test_eq(integer: Integer, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.integer.Integer.__eq__."""
    equality: bool = integer == other

    assert equality == expected_equality
