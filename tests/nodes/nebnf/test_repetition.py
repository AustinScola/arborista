"""Test arborista.nodes.nebnf.repetition."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.repetition import Repetition
from arborista.nodes.nebnf.righthand_side import RighthandSide
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.repetition.Repetition inheritance."""
    assert issubclass(Repetition, NEBNFNode)


# yapf: disable
@pytest.mark.parametrize('element, parent, pass_parent', [
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), None, False),
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), None, True),
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), MagicMock(Node), True),
    (RighthandSide(Identifier(UppercaseLetter('F'), [])), MagicMock(Node), True),
])
# yapf: enable
def test_init(element: RighthandSide, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.repetition.Repetition.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    repetition: Repetition = Repetition(element, **keyword_arguments)

    assert repetition.element == element
    assert repetition.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('repetition, other, expected_equality', [
    (Repetition(RighthandSide(Identifier(UppercaseLetter('F'), []))), 1, False),
    (Repetition(RighthandSide(Identifier(UppercaseLetter('F'), []))), 'F', False),
    (Repetition(RighthandSide(Identifier(UppercaseLetter('F'), []))), Repetition(RighthandSide(Identifier(UppercaseLetter('B'), []))), False),
    (Repetition(RighthandSide(Identifier(UppercaseLetter('F'), []))), Repetition(RighthandSide(Identifier(UppercaseLetter('F'), []))), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(repetition: Repetition, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.repetition.Repetition.__eq__."""
    equality: bool = repetition == other

    assert equality == expected_equality
