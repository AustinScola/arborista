"""Test arborista.nodes.nebnf.uppercase_letter."""
import string
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest
from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter, UppercaseLetterValue


def test_uppercase_letter_value() -> None:
    """Test arborista.nodes.nebnf.uppercase_letter.UppercaseLetterValue."""
    assert isinstance(UppercaseLetterValue, type(Literal))
    assert UppercaseLetterValue.__values__ == tuple(  # type: ignore[attr-defined]
        string.ascii_uppercase)


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.uppercase_letter.UppercaseLetter inheritance."""
    assert issubclass(UppercaseLetter, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    ('A', None, False),
    ('A', None, True),
    ('A', MagicMock(Node), True),
    ('B', MagicMock(Node), True),
])
# yapf: enable
def test_init(value: UppercaseLetterValue, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.uppercase_letter.UppercaseLetter.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    uppercase_letter: UppercaseLetter = UppercaseLetter(value, **keyword_arguments)

    assert uppercase_letter.value == value
    assert uppercase_letter.parent is parent
