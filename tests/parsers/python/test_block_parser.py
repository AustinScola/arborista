"""Test arborista.parsers.python.block_parser."""
import libcst
import pytest

from arborista.nodes.python.block import Block
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.parser import Parser
from arborista.parsers.python.block_parser import BlockParser, LibcstBlock
from testing_helpers.assert_parent_set_in_children import assert_parent_set_in_children


def test_inheritance() -> None:
    """Test arborista.parsers.python.block_parser.BlockParser inheritance."""
    assert issubclass(BlockParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_block, expected_block', [
    (libcst.IndentedBlock([libcst.SimpleStatementLine([libcst.Return()])]), Block([SimpleStatement(small_statements=[ReturnStatement()])], '   ')),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_block(libcst_block: LibcstBlock, expected_block: Block) -> None:
    """Test arborista.parsers.python.block_parser.BlockParser.parse_block."""
    block: Block = BlockParser.parse_block(libcst_block)

    assert block == expected_block
    assert_parent_set_in_children(block)
