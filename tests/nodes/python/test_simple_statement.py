"""Test arborista.nodes.python.simple_statement."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.small_statement import SmallStatements
from arborista.nodes.python.statement import Statement
from arborista.nodes.python.trailing_whitespace import TrailingWhitespace


def test_inheritance() -> None:
    """Test arborista.nodes.python.simple_statement.SimpleStatement inheritance."""
    assert issubclass(SimpleStatement, Statement)


_PARENT = MagicMock()


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, keyword_arguments, expected_small_statements, expected_trailing_whitespace, expected_parent', [
    ([[]], {}, [], TrailingWhitespace(), None),
    ([[]], {'parent': None}, [], TrailingWhitespace(), None),
    ([[]], {'parent': _PARENT}, [], TrailingWhitespace(), _PARENT),
    ([[PassStatement()]], {'parent': _PARENT}, [PassStatement()], TrailingWhitespace(), _PARENT),
    ([[PassStatement()]], {'trailing_whitespace': TrailingWhitespace()}, [PassStatement()], TrailingWhitespace(), None),
])
# yapf: enable # pylint: enable=line-too-long
def test_simple_statement_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
                               expected_small_statements: SmallStatements,
                               expected_trailing_whitespace: Optional[TrailingWhitespace],
                               expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.simple_statement.__init__."""
    simple_statement: SimpleStatement = SimpleStatement(*arguments, **keyword_arguments)

    assert simple_statement.small_statements == expected_small_statements
    assert simple_statement.trailing_whitespace == expected_trailing_whitespace
    assert simple_statement.parent is expected_parent


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
