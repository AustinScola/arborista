"""Test arborista.python.nodes.block."""
from typing import Any

import pytest

from arborista.nodes.python.block import Block
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.statement import StatementList, Statements


def test_inheritance() -> None:
    """Test arborista.nodes.python.block.Block inheritance."""
    assert issubclass(Block, PythonNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('body, expected_body, indent', [
    ([ReturnStatement()], [ReturnStatement()], '    '),
    ([ReturnStatement()], [ReturnStatement()], '\t'),
    ([ReturnStatement(), ReturnStatement(), ReturnStatement()], [ReturnStatement(), ReturnStatement(), ReturnStatement()], '    '),
    ([ReturnStatement(), ReturnStatement(), ReturnStatement()], [ReturnStatement(), ReturnStatement(), ReturnStatement()], '\t'),
    (iter([]), [], '   '),
    (iter([]), [], '\t'),
    (iter([ReturnStatement(), ReturnStatement(), ReturnStatement()]), [ReturnStatement(), ReturnStatement(), ReturnStatement()], '    '),
    (iter([ReturnStatement(), ReturnStatement(), ReturnStatement()]), [ReturnStatement(), ReturnStatement(), ReturnStatement()], '\t'),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(body: Statements, expected_body: StatementList, indent: str) -> None:
    """Test arborista.nodes.python.block.Block.__init__."""
    block: Block = Block(body, indent)

    assert block.body == expected_body
    assert block.indent == indent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('block, other, expected_equality', [
    (Block([SimpleStatement([ReturnStatement()])], '   '), 'foo', False),
    (Block([SimpleStatement([ReturnStatement()])], '   '), Block([SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()])], '   '), False),
    (Block([SimpleStatement([ReturnStatement()])], '   '), Block([SimpleStatement([ReturnStatement()])], '   '), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(block: Block, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.block.Block.__eq__."""
    equality: bool = block == other
    assert equality == expected_equality
