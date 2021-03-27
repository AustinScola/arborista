"""Test arborista.nodes.nebnf.concatenation."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.concatenation import Concatenation
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.righthand_side import RighthandSide
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.concatenation.Concatenation inheritance."""
    assert issubclass(Concatenation, NEBNFNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('first, second, parent, pass_parent', [
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), None, False),
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), None, True),
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), MagicMock(Node), True),
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), MagicMock(Node), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(first: RighthandSide, second: RighthandSide, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.concatenation.Concatenation.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    concatenation: Concatenation = Concatenation(first, second, **keyword_arguments)

    assert concatenation.first == first
    assert concatenation.second == second
    assert concatenation.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('concatenation, other, expected_equality', [
    (Concatenation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), 1, False),
    (Concatenation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), 'F', False),
    (Concatenation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), Concatenation(RighthandSide(Identifier(UppercaseLetter('S'), [])), RighthandSide(Identifier(UppercaseLetter('E'), []))), False),
    (Concatenation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), Concatenation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('E'), []))), False),
    (Concatenation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), Concatenation(RighthandSide(Identifier(UppercaseLetter('S'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), False),
    (Concatenation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), Concatenation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(concatenation: Concatenation, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.concatenation.Concatenation.__eq__."""
    equality: bool = concatenation == other

    assert equality == expected_equality
