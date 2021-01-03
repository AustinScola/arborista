"""Test arborista.nodes.python.simple_string."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node
from arborista.nodes.python.simple_string import SimpleString
from arborista.nodes.python.string import String
from testing_helpers.animal_nodes import Dog


def test_inheritance() -> None:
    """Test arborista.nodes.python.simple_string.SimpleString inheritance."""
    assert issubclass(SimpleString, String)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent, expected_parent', [
    ('foo', None, False, None),
    ('foo', None, True, None),
    ('foo', Dog(), True, Dog()),
])
# yapf: enable
def test_init(value: str, parent: Optional[Node], pass_parent: bool,
              expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.simple_string.SimpleString.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    simple_string = SimpleString(value, **keyword_arguments)

    assert simple_string.value == value
    assert simple_string.parent == expected_parent


# yapf: disable
@pytest.mark.parametrize('simple_string, other, expected_equality', [
    (SimpleString(''), '', False),
    (SimpleString('foo'), SimpleString(''), False),
    (SimpleString(''), SimpleString('foo'), False),
    (SimpleString('foo'), SimpleString('bar'), False),
    (SimpleString(''), SimpleString(''), True),
    (SimpleString('foo'), SimpleString('foo'), True),
])
# yapf: enable
def test_eq(simple_string: SimpleString, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.simple_string.SimpleString.__eq__."""
    equality: bool = simple_string == other

    assert equality == expected_equality
