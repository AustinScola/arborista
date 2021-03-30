"""Test arborista.nodes.nebnf.grouping."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.grouping import Grouping
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetter
from arborista.nodes.nebnf.name import Name
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.righthand_side import RighthandSide
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.grouping.Grouping inheritance."""
    assert issubclass(Grouping, NEBNFNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('name, righthand_side, parent, pass_parent', [
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
def test_init(name: Optional[Name], righthand_side: RighthandSide, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.grouping.Grouping.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    grouping: Grouping = Grouping(name, righthand_side, **keyword_arguments)

    assert grouping.name == name
    assert grouping.righthand_side == righthand_side
    assert grouping.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('grouping, other, expected_equality', [
    (Grouping(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), 1, False),
    (Grouping(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), 'F', False),
    (Grouping(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), Grouping(Name(LowercaseLetter('m'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), False),
    (Grouping(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), Grouping(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('B'), []))), False),
    (Grouping(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), Grouping(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(grouping: Grouping, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.grouping.Grouping.__eq__."""
    equality: bool = grouping == other

    assert equality == expected_equality
