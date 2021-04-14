"""Test arborista.nodes.nebnf.letter."""
from typing import Any, Dict, Optional, Union
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.letter import Letter, LetterValue
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetterValue
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetterValue


def test_letter_value() -> None:
    """Test arborista.nodes.nebnf.letter.LetterValue."""
    assert isinstance(LetterValue, type(Union))
    assert LetterValue.__args__ == (  # type: ignore[attr-defined]
        LowercaseLetterValue, UppercaseLetterValue)


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.letter.Letter inheritance."""
    assert issubclass(Letter, NEBNFNode)


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
def test_init(value: LetterValue, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.letter.Letter.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    letter: Letter = Letter(value, **keyword_arguments)

    assert letter.value == value
    assert letter.parent is parent
