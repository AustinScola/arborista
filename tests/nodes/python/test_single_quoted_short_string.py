"""Test arborista.nodes.python.single_quoted_short_string."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.short_string import ShortString
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString


def test_inheritance() -> None:
    """Test arborista.nodes.python.single_quoted_short_string.SingleQuotedShortString inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(SingleQuotedShortString, ShortString)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    ('foo', None, False),
    ('foo', None, True),
    ('foo', MagicMock(), True),
])
# yapf: enable
def test_init(value: str, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.single_quoted_short_string.SingleQuotedShortString.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    single_quoted_short_string: SingleQuotedShortString = SingleQuotedShortString(
        value, **keyword_arguments)

    assert single_quoted_short_string.value == value
    assert single_quoted_short_string.parent is parent


# yapf: disable
@pytest.mark.parametrize('single_quoted_short_string, other, expected_equality', [
    (SingleQuotedShortString('foo'), 'foo', False),
    (SingleQuotedShortString('foo'), SingleQuotedShortString('bar'), False),
    (SingleQuotedShortString('foo'), SingleQuotedShortString('foo'), True),
])
# yapf: enable
def test_eq(single_quoted_short_string: SingleQuotedShortString, other: Any,
            expected_equality: bool) -> None:
    """Test arborista.nodes.python.single_quoted_short_string.SingleQuotedShortString.__eq__."""
    equality: bool = single_quoted_short_string == other

    assert equality == expected_equality
