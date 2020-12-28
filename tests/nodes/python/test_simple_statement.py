"""Test arborista.nodes.python.simple_statement."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.block import Block
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.small_statement import SmallStatements
from arborista.nodes.python.statement import Statement


def test_inheritance() -> None:
    """Test arborista.nodes.python.simple_statement.SimpleStatement inheritance."""
    assert issubclass(SimpleStatement, Statement)


# yapf: disable
@pytest.mark.parametrize('small_statements, parent, pass_parent', [
    ([], None, False),
    ([], None, True),
    ([], Block([SimpleStatement([])], '    '), True),
])
# yapf: enable
def test_simple_statement_init(small_statements: SmallStatements, parent: Optional[Node],
                               pass_parent: bool) -> None:
    """Test arborista.nodes.python.simple_statement.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    simple_statement: SimpleStatement = SimpleStatement(small_statements, **keyword_arguments)

    assert simple_statement.small_statements == small_statements
    assert id(simple_statement.parent) == id(parent)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('simple_statement, other, expected_equality', [
    (SimpleStatement(small_statements=[ReturnStatement()]), 'foo', False),
    (SimpleStatement(small_statements=[ReturnStatement()]), SimpleStatement(small_statements=[ReturnStatement()]), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(simple_statement: SimpleStatement, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.simple_statement.__eq__."""
    equality: bool = simple_statement == other

    assert equality == expected_equality


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('simple_statement, expected_children_list', [
    (SimpleStatement(small_statements=[]), []),
    (SimpleStatement(small_statements=[ReturnStatement()]), [ReturnStatement()]),
    (SimpleStatement(small_statements=[ReturnStatement(), ReturnStatement(), ReturnStatement()]), [ReturnStatement(), ReturnStatement(), ReturnStatement()]),
])
# yapf: enable # pylint: enable=line-too-long
def test_iterate_children(simple_statement: SimpleStatement,
                          expected_children_list: NodeList) -> None:
    """Test arborista.nodes.python.simple_statement.iterate_children."""
    children: NodeIterator = simple_statement.iterate_children()
    children_list: NodeList = list(children)

    assert children_list == expected_children_list
