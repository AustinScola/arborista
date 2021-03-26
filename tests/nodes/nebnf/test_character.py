"""Test arborista.nodes.nebnf.character."""
from typing import Any, Dict, Optional, Union
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.character import Character, CharacterValue
from arborista.nodes.nebnf.digit import DigitValue
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetterValue
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.symbol import SymbolValue
from arborista.nodes.nebnf.underscore import UnderscoreValue
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetterValue


def test_character_value() -> None:
    """Test arborista.nodes.nebnf.character.CharacterValue."""
    assert isinstance(CharacterValue, type(Union))
    assert CharacterValue.__args__ == (  # type: ignore[attr-defined]
        LowercaseLetterValue, UppercaseLetterValue, DigitValue, SymbolValue, UnderscoreValue)


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.character.Character inheritance."""
    assert issubclass(Character, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    ('a', None, False),
    ('a', None, True),
    ('A', None, False),
    ('A', None, True),
    ('a', MagicMock(Node), True),
    ('A', MagicMock(Node), True),
])
# yapf: enable
def test_init(value: CharacterValue, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.character.Character.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    character: Character = Character(value, **keyword_arguments)

    assert character.value == value
    assert character.parent is parent


# yapf: disable
@pytest.mark.parametrize('character, other, expected_equality', [
    (Character('a'), 1, False),
    (Character('a'), 'a', False),
    (Character('a'), Character('b'), False),
    (Character('a'), Character('a'), True),
])
# yapf: enable
def test_eq(character: Character, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.character.Character.__eq__."""
    equality: bool = character == other

    assert equality == expected_equality
