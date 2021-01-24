"""Test arborista.nodes.python.boolean_operation."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.and_ import And
from arborista.nodes.python.boolean_operation import BooleanOperation
from arborista.nodes.python.boolean_operator import BooleanOperator
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.name import Name
from arborista.nodes.python.or_ import Or


def test_inheritance() -> None:
    """Test arborista.nodes.python.boolean_operation.BooleanOperation inheritance."""
    assert issubclass(BooleanOperation, Expression)


# yapf: disable
@pytest.mark.parametrize('left, operator, right, parent, pass_parent', [
    (Name('a'), And(), Name('b'), None, False),
    (Name('a'), And(), Name('b'), None, True),
    (Name('a'), And(), Name('b'), MagicMock(), True),
])
# yapf: enable
def test_init(left: Expression, operator: BooleanOperator, right: Expression,
              parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.boolean_operation.BooleanOperation.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    boolean_operation: BooleanOperation = BooleanOperation(left, operator, right,
                                                           **keyword_arguments)

    assert boolean_operation.left == left
    assert boolean_operation.operator == operator
    assert boolean_operation.right == right
    assert boolean_operation.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('boolean_operation, other, expected_equality', [
    (BooleanOperation(Name('a'), And(), Name('b')), 'foo', False),
    (BooleanOperation(Name('a'), And(), Name('b')), BooleanOperation(Name('b'), And(), Name('b')), False),
    (BooleanOperation(Name('a'), And(), Name('b')), BooleanOperation(Name('a'), Or(), Name('b')), False),
    (BooleanOperation(Name('a'), And(), Name('b')), BooleanOperation(Name('a'), And(), Name('a')), False),
    (BooleanOperation(Name('a'), And(), Name('b')), BooleanOperation(Name('a'), And(), Name('b')), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(boolean_operation: BooleanOperation, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.boolean_operation.BooleanOperation.__eq__."""
    equality: bool = boolean_operation == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('boolean_operation, expected_children_list', [
    (BooleanOperation(Name('a'), And(), Name('b')), [Name('a'), And(), Name('b')]),
])
# yapf: enable
def test_iterate_children(boolean_operation: BooleanOperation,
                          expected_children_list: NodeList) -> None:
    """Test arborista.nodes.python.boolean_operation.BooleanOperation.iterate_children."""
    children: NodeIterator = boolean_operation.iterate_children()
    children_list: NodeList = list(children)

    assert children_list == expected_children_list
