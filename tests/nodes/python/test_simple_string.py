"""Test arborista.nodes.python.simple_string."""
from typing import Any, Dict, List, Optional

import pytest

from arborista.node import Node
from arborista.nodes.python.simple_string import SimpleString
from arborista.nodes.python.string import String
from testing_helpers.animal_nodes import Dog


def test_inheritance() -> None:
    """Test arborista.nodes.python.simple_string.SimpleString inheritance."""
    assert issubclass(SimpleString, String)


# yapf: disable
@pytest.mark.parametrize('value, pass_value, parent, pass_parent, expected_value', [
    (None, False, None, False, ''),
    ('', False, None, True, ''),
    ('foo', True, None, False, 'foo'),
    ('foo', True, None, True, 'foo'),
    ('foo', True, Dog(), True, 'foo'),
])
# yapf: enable
def test_init(value: Optional[str], pass_value: bool, parent: Optional[Node], pass_parent: bool,
              expected_value: str) -> None:
    """Test arborista.nodes.python.simple_string.SimpleString.__init__."""
    arguments: List[Any] = []
    if pass_value:
        arguments.append(value)

    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    simple_string = SimpleString(*arguments, **keyword_arguments)

    assert simple_string.value == expected_value
    assert simple_string.parent is parent


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
