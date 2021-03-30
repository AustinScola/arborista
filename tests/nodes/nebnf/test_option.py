"""Test arborista.nodes.nebnf.option."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetter
from arborista.nodes.nebnf.name import Name
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.option import Option
from arborista.nodes.nebnf.righthand_side import RighthandSide
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.option.Option inheritance."""
    assert issubclass(Option, NEBNFNode)


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
    """Test arborista.nodes.nebnf.option.Option.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    option: Option = Option(name, righthand_side, **keyword_arguments)

    assert option.name == name
    assert option.righthand_side == righthand_side
    assert option.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('option, other, expected_equality', [
    (Option(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), 1, False),
    (Option(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), 'F', False),
    (Option(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), Option(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('B'), []))), False),
    (Option(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), Option(Name(LowercaseLetter('m'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), False),
    (Option(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), Option(Name(LowercaseLetter('n'), []), RighthandSide(Identifier(UppercaseLetter('F'), []))), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(option: Option, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.nebnf.option.Option.__eq__."""
    equality: bool = option == other

    assert equality == expected_equality
