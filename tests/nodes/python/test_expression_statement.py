"""Test arborista.nodes.python.expression_statement."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.expression_statement import ExpressionStatement
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.small_statement import SmallStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.expression_statement.ExpressionStatement inheritance."""
    assert issubclass(ExpressionStatement, SmallStatement)


# yapf: disable
@pytest.mark.parametrize('expression, parent, pass_parent', [
    (Integer(1), None, False),
    (Integer(1), None, True),
    (Integer(1), MagicMock(), True),
])
# yapf: enable
def test_init(expression: Expression, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.expression_statement.ExpressionStatement.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    expression_statement: ExpressionStatement = ExpressionStatement(expression, **keyword_arguments)

    assert expression_statement.expression == expression
    assert expression_statement.parent is parent


# yapf: disable
@pytest.mark.parametrize('expression_statement, other, expected_equality', [
    (ExpressionStatement(Integer(5)), 'foo', False),
    (ExpressionStatement(Integer(5)), ExpressionStatement(Integer(7)), False),
    (ExpressionStatement(Integer(5)), ExpressionStatement(Integer(5)), True),
])
# yapf: enable
def test_eq(expression_statement: ExpressionStatement, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.expression_statement.ExpressionStatement.__eq__."""
    equality: bool = expression_statement == other

    assert equality == expected_equality
