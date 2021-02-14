"""Test arborista.nodes.sequences.text.string."""
from typing import Any, Dict, List, Optional

import pytest

from arborista.node import Node
from arborista.nodes.sequences.text.string import String
from testing_helpers.animal_nodes import Dog


def test_inheritance() -> None:
    """Test arborista.nodes.sequences.text.string.String inheritance."""
    assert issubclass(String, Node)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('value, pass_value, parent, pass_parent, expected_value', [
    (None, False, None, False, ''),
    (None, False, Dog(), True, ''),
    ('foo', True, None, False, 'foo'),
    ('foo', True, None, True, 'foo'),
    ('foo', True, Dog(), True, 'foo'),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_init(value: Optional[str], pass_value: bool, parent: Optional[Node], pass_parent: bool,
              expected_value: str) -> None:
    """Test arborista.nodes.sequences.text.string.String.__init__."""
    arguments: List[Any] = []
    if pass_value:
        arguments.append(value)

    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    string: String = String(*arguments, **keyword_arguments)

    assert string.value == expected_value
    assert string.parent is parent


# yapf: disable
@pytest.mark.parametrize('string, other, expected_equality', [
    (String('foo'), 'foo', False),
    (String('foo'), String('bar'), False),
    (String('foo'), String('foo'), True),
])
# yapf: enable
def test_eq(string: String, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.sequences.text.string.String.__eq__."""
    equality: bool = string == other

    assert equality == expected_equality
