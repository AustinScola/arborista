"""Test arborista.nodes.python.simple_statement."""
from typing import Any

import pytest

from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.small_statement import SmallStatements
from arborista.nodes.python.statement import Statement


def test_inheritance() -> None:
    """Test arborista.nodes.python.simple_statement.SimpleStatement inheritance."""
    assert issubclass(SimpleStatement, Statement)


# yapf: disable
@pytest.mark.parametrize('small_statements', [
    ([]),
])
# yapf: enable
def test_simple_statement_init(small_statements: SmallStatements) -> None:
    """Test arborista.nodes.python.simple_statement.__init__."""
    simple_statement: SimpleStatement = SimpleStatement(small_statements)

    assert simple_statement.small_statements == small_statements


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
