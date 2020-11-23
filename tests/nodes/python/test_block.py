"""Test arborista.python.nodes.block."""
import pytest

from arborista.nodes.python.block import Block
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.statement import Statement, StatementList, Statements


def test_inheritance() -> None:
    """Test arborista.nodes.python.block.Block inheritance."""
    assert issubclass(Block, PythonNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('first_statement, rest_of_statements, expected_body', [
    (ReturnStatement(), [], [ReturnStatement()]),
    (ReturnStatement(), [ReturnStatement()], [ReturnStatement(), ReturnStatement()]),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(first_statement: Statement, rest_of_statements: Statements,
              expected_body: StatementList) -> None:
    """Test arborista.nodes.python.block.Block.__init__."""
    block: Block = Block(first_statement, rest_of_statements)

    assert block.body == expected_body
