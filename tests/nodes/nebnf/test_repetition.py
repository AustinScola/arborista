"""Test arborista.nodes.nebnf.repetition."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetter
from arborista.nodes.nebnf.name import Name
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.repetition import Repetition
from arborista.nodes.nebnf.righthand_side import RighthandSide
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.repetition.Repetition inheritance."""
    assert issubclass(Repetition, NEBNFNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('name, element, parent, pass_parent', [
    (None, RighthandSide(Identifier(UppercaseLetter('F'), [])), None, False),
    (None, RighthandSide(Identifier(UppercaseLetter('F'), [])), None, True),
    (None, RighthandSide(Identifier(UppercaseLetter('F'), [])), MagicMock(Node), True),
    (None, RighthandSide(Identifier(UppercaseLetter('F'), [])), MagicMock(Node), True),
    (Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), [])), None, False),
    (Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), [])), None, True),
    (Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), [])), MagicMock(Node), True),
    (Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), [])), MagicMock(Node), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(name: Optional[Name], element: RighthandSide, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.repetition.Repetition.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    repetition: Repetition = Repetition(name, element, **keyword_arguments)

    assert repetition.name == name
    assert repetition.element == element
    assert repetition.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('repetition, other, expected_equality', [
    (Repetition(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), 1, False),
    (Repetition(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), 'F', False),
    (Repetition(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), Repetition(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('B'), []))), False),
    (Repetition(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), Repetition(Name(LowercaseLetter('m'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), False),
    (Repetition(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), Repetition(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(repetition: Repetition, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.repetition.Repetition.__eq__."""
    equality: bool = repetition == other

    assert equality == expected_equality
