"""Test arborista.nodes.nebnf.grammer."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.grammer import Grammer
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.lefthand_side import LefthandSide
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.righthand_side import RighthandSide
from arborista.nodes.nebnf.rule import Rule
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.grammer.Grammer inheritance."""
    assert issubclass(Grammer, NEBNFNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('rules, parent, pass_parent', [
    ([], None, False),
    ([], MagicMock(), True),
    ([Grammer([Rule(LefthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])))])], None, False),
    ([Grammer([Rule(LefthandSide(Identifier(UppercaseLetter('F'), [])), RighthandSide(Identifier(UppercaseLetter('B'), [])))])], MagicMock(), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(rules: List[Rule], parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.grammer.Grammer.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    grammer: Grammer = Grammer(rules, **keyword_arguments)

    assert grammer.rules == rules
    assert grammer.parent is parent
