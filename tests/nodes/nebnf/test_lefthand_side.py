"""Test arborista.nodes.nebnf.lefthand_side."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.lefthand_side import LefthandSide
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.lefthand_side.LefthandSide inheritance."""
    assert issubclass(LefthandSide, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('identifier, parent, pass_parent', [
    ('a', None, False),
    ('a', None, True),
    ('A', None, False),
    ('A', None, True),
    ('a', MagicMock(Node), True),
    ('A', MagicMock(Node), True),
])
# yapf: enable
def test_init(identifier: Identifier, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.lefthand_side.LefthandSide.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    lefthand_side: LefthandSide = LefthandSide(identifier, **keyword_arguments)

    assert lefthand_side.identifier == identifier
    assert lefthand_side.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('lefthand_side, other, expected_equality', [
    (LefthandSide(Identifier(UppercaseLetter('F'), [])), 1, False),
    (LefthandSide(Identifier(UppercaseLetter('F'), [])), 'F', False),
    (LefthandSide(Identifier(UppercaseLetter('F'), [])), LefthandSide(Identifier(UppercaseLetter('B'), [])), False),
    (LefthandSide(Identifier(UppercaseLetter('F'), [])), LefthandSide(Identifier(UppercaseLetter('F'), [])), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(lefthand_side: LefthandSide, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.lefthand_side.LefthandSide.__eq__."""
    equality: bool = lefthand_side == other

    assert equality == expected_equality
