"""Test arborista.nodes.python.for_statement."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.expression_list import ExpressionList
from arborista.nodes.python.for_statement import ForStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite


def test_inheritance() -> None:
    """Test arborista.nodes.python.for_statement.ForStatement inheritance."""
    assert issubclass(ForStatement, CompoundStatement)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('values, sources, body, else_, parent, pass_parent', [
    (ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), None, None, False),
    (ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), None, None, True),
    (ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), None, MagicMock(), True),
    (ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), Else(SimpleStatement([PassStatement()])), None, True),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_init(values: ExpressionList, sources: ExpressionList, body: Suite, else_: Optional[Else],
              parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.for_statement.ForStatement.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    for_statement: ForStatement = ForStatement(values, sources, body, else_, **keyword_arguments)

    assert for_statement.values == values
    assert for_statement.sources == sources
    assert for_statement.body == body
    assert for_statement.else_ == else_
    assert for_statement.parent is parent
