"""Test arborista.nodes.nebnf.rule."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.lefthand_side import LefthandSide
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.righthand_side import RighthandSide
from arborista.nodes.nebnf.rule import Rule
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.rule.Rule inheritance."""
    assert issubclass(Rule, NEBNFNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('lefthand_side, righthand_side, parent, pass_parent', [
    (LefthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), None, False),
    (LefthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), None, True),
    (LefthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), MagicMock(Node), True),
    (LefthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])), MagicMock(Node), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(lefthand_side: LefthandSide, righthand_side: RighthandSide, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.rule.Rule.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    rule: Rule = Rule(lefthand_side, righthand_side, **keyword_arguments)

    assert rule.lefthand_side == lefthand_side
    assert rule.righthand_side == righthand_side
    assert rule.parent is parent
