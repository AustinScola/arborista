"""Test arborista.nodes.nebnf.righthand_side."""
from typing import Any, Dict, Optional, Union
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.nebnf.alternation import Alternation
from arborista.nodes.nebnf.concatenation import Concatenation
from arborista.nodes.nebnf.grouping import Grouping
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.option import Option
from arborista.nodes.nebnf.repetition import Repetition
from arborista.nodes.nebnf.righthand_side import Expression, RighthandSide
from arborista.nodes.nebnf.terminal import Terminal
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetter


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.righthand_side.RighthandSide inheritance."""
    assert issubclass(RighthandSide, NEBNFNode)


def test_expression() -> None:
    """Test arborista.nodes.nebnf.righthand_side.Expression."""
    assert isinstance(Expression, type(Union))
    assert Expression.__args__ == (  # type: ignore[attr-defined]
        Terminal, Identifier, Option, Grouping, Repetition, Alternation, Concatenation)


# yapf: disable
@pytest.mark.parametrize('expression, parent, pass_parent', [
    (Identifier(UppercaseLetter('F'), []), None, False),
    (Identifier(UppercaseLetter('F'), []), None, True),
    (Identifier(UppercaseLetter('F'), []), None, False),
    (Identifier(UppercaseLetter('F'), []), None, True),
    (Identifier(UppercaseLetter('F'), []), MagicMock(Node), True),
    (Identifier(UppercaseLetter('F'), []), MagicMock(Node), True),
])
# yapf: enable
def test_init(expression: Expression, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.nebnf.righthand_side.RighthandSide.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    righthand_side: RighthandSide = RighthandSide(expression, **keyword_arguments)

    assert righthand_side.expression == expression
    assert righthand_side.parent is parent
