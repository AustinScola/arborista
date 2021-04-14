"""Test arborista.nodes.python.string."""
from typing import Any, Dict, Optional, Union

import pytest

from arborista.node import Node
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.long_string import LongString
from arborista.nodes.python.short_string import ShortString
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String, StringValue
from arborista.nodes.python.string_prefix import StringPrefix


def test_string_value() -> None:
    """Test arborista.nodes.python.string.String.StringValue."""
    assert isinstance(StringValue, type(Union))
    assert StringValue.__args__ == (ShortString, LongString)  # type: ignore[attr-defined]


def test_inheritance() -> None:
    """Test arborista.nodes.python.string.String inheritance."""
    assert issubclass(String, Atom)


# yapf: disable
@pytest.mark.parametrize('prefix, value, parent, pass_parent', [
    (None, SingleQuotedShortString(''), None, False),
    (None, SingleQuotedShortString(''), None, True),
    (StringPrefix('f'), SingleQuotedShortString(''), None, True),
])
# yapf: enable
def test_init(prefix: Optional[StringPrefix], value: StringValue, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.string.String.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    string: String = String(prefix, value, **keyword_arguments)

    assert string.prefix == prefix
    assert string.value == value
    assert string.parent is parent
