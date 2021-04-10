"""Test arborista.nodes.python.single_quoted_long_string."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.long_string import LongString
from arborista.nodes.python.single_quoted_long_string import SingleQuotedLongString


def test_inheritance() -> None:
    """Test arborista.nodes.python.single_quoted_long_string.SingleQuotedLongString inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(SingleQuotedLongString, LongString)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    ('foo', None, False),
    ('foo', None, True),
    ('foo', MagicMock(), True),
])
# yapf: enable
def test_init(value: str, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.single_quoted_long_string.SingleQuotedLongString.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    single_quoted_long_string: SingleQuotedLongString = SingleQuotedLongString(
        value, **keyword_arguments)

    assert single_quoted_long_string.value == value
    assert single_quoted_long_string.parent is parent


# yapf: disable
@pytest.mark.parametrize('single_quoted_long_string, other, expected_equality', [
    (SingleQuotedLongString('foo'), 'foo', False),
    (SingleQuotedLongString('foo'), SingleQuotedLongString('bar'), False),
    (SingleQuotedLongString('foo'), SingleQuotedLongString('foo'), True),
])
# yapf: enable
def test_eq(single_quoted_long_string: SingleQuotedLongString, other: Any,
            expected_equality: bool) -> None:
    """Test arborista.nodes.python.single_quoted_long_string.SingleQuotedLongString.__eq__."""
    equality: bool = single_quoted_long_string == other

    assert equality == expected_equality
