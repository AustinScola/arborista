"""Test arborista.nodes.python.if_statement."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.elif_ import Elifs
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.if_ import If
from arborista.nodes.python.if_statement import IfStatement
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.if_statement.IfStatement inheritance."""
    assert issubclass(IfStatement, CompoundStatement)


# yapf: disable
@pytest.mark.parametrize('if_, elifs, else_, parent, pass_parent', [
    (If(Integer(1), SimpleStatement([PassStatement()])), [], None, None, False),
])
# yapf: enable
def test_init(if_: If, elifs: Elifs, else_: Optional[Else], parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.if_statement.IfStatement.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    if_statement: IfStatement = IfStatement(if_, elifs, else_, **keyword_arguments)

    assert if_statement.if_ == if_
    assert if_statement.elifs == elifs
    assert if_statement.else_ == else_
    assert if_statement.parent is parent
