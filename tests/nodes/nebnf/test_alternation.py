"""Test arborista.nodes.nebnf.alternation."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.alternation import Alternation
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.righthand_side import RighthandSide
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.alternation.Alternation inheritance."""
    assert issubclass(Alternation, NEBNFNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('first_choice, second_choice, parent, pass_parent', [
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), None, False),
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), None, True),
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), MagicMock(Node), True),
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), MagicMock(Node), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(first_choice: RighthandSide, second_choice: RighthandSide, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.alternation.Alternation.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    alternation: Alternation = Alternation(first_choice, second_choice, **keyword_arguments)

    assert alternation.first_choice == first_choice
    assert alternation.second_choice == second_choice
    assert alternation.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('alternation, other, expected_equality', [
    (Alternation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), 1, False),
    (Alternation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), 'F', False),
    (Alternation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), Alternation(RighthandSide(Identifier(UppercaseLetter('S'), [])), RighthandSide(Identifier(UppercaseLetter('E'), []))), False),
    (Alternation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), Alternation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('E'), []))), False),
    (Alternation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), Alternation(RighthandSide(Identifier(UppercaseLetter('S'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), False),
    (Alternation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), Alternation(RighthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), []))), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(alternation: Alternation, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.alternation.Alternation.__eq__."""
    equality: bool = alternation == other

    assert equality == expected_equality
