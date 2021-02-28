"""Test arborista.nodes.nebnf.digit."""
import string
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest
from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.digit import Digit, DigitValue
from arborista.nodes.nebnf.nebnf_node import NEBNFNode


def test_digit_value() -> None:
    """Test arborista.nodes.nebnf.digit.DigitValue."""
    assert isinstance(DigitValue, type(Literal))
    assert DigitValue.__values__ == tuple(string.digits)  # type: ignore[attr-defined]


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.digit.Digit inheritance."""
    assert issubclass(Digit, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent', [
    ('0', None, False),
    ('0', None, True),
    ('0', MagicMock(Node), True),
    ('1', MagicMock(Node), True),
])
# yapf: enable
def test_init(value: DigitValue, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.digit.Digit.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    digit: Digit = Digit(value, **keyword_arguments)

    assert digit.value == value
    assert digit.parent is parent


# yapf: disable
@pytest.mark.parametrize('digit, other, expected_equality', [
    (Digit('0'), 0, False),
    (Digit('0'), '0', False),
    (Digit('0'), Digit('1'), False),
    (Digit('0'), Digit('0'), True),
])
# yapf: enable
def test_eq(digit: Digit, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.digit.Digit.__eq__."""
    equality: bool = digit == other

    assert equality == expected_equality
