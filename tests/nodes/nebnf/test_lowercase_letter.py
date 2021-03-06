"""Test arborista.nodes.nebnf.lowercase_letter."""
import string
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest
from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetter, LowercaseLetterValue
from arborista.nodes.nebnf.nebnf_node import NEBNFNode


def test_lowercase_letter_value() -> None:
    """Test arborista.nodes.nebnf.lowercase_letter.LowercaseLetterValue."""
    assert isinstance(LowercaseLetterValue, type(Literal))
    assert LowercaseLetterValue.__values__ == tuple(  # type: ignore[attr-defined]
        string.ascii_lowercase)


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.lowercase_letter.LowercaseLetter inheritance."""
    assert issubclass(LowercaseLetter, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    ('a', None, False),
    ('a', None, True),
    ('a', MagicMock(Node), True),
    ('b', MagicMock(Node), True),
])
# yapf: enable
def test_init(value: LowercaseLetterValue, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.lowercase_letter.LowercaseLetter.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    lowercase_letter: LowercaseLetter = LowercaseLetter(value, **keyword_arguments)

    assert lowercase_letter.value == value
    assert lowercase_letter.parent is parent


# yapf: disable
@pytest.mark.parametrize('lowercase_letter, other, expected_equality', [
    (LowercaseLetter('a'), 1, False),
    (LowercaseLetter('a'), 'a', False),
    (LowercaseLetter('a'), LowercaseLetter('b'), False),
    (LowercaseLetter('a'), LowercaseLetter('a'), True),
])
# yapf: enable
def test_eq(lowercase_letter: LowercaseLetter, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.lowercase_letter.LowercaseLetter.__eq__."""
    equality: bool = lowercase_letter == other

    assert equality == expected_equality
