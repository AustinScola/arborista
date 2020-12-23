"""Test arborista.nodes.sequences.text.string."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node
from arborista.nodes.sequences.text.string import String
from testing_helpers.animal_nodes import Dog


def test_inheritance() -> None:
    """Test arborista.nodes.sequences.text.string.String inheritance."""
    assert issubclass(String, Node)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent, expected_parent', [
    ('foo', None, False, None),
    ('foo', None, True, None),
    ('foo', Dog(), True, Dog()),
])
# yapf: enable
def test_init(value: str, parent: Optional[Node], pass_parent: bool,
              expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.sequences.text.string.String.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    string: String = String(value, **keyword_arguments)

    assert string.value == value
    assert string.parent == expected_parent


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
