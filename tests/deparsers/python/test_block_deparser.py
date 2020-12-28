"""Test arborista.deparsers.python.block_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.block_deparser import BlockDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.block_deparser.BlockDeparser inheritance."""
    assert issubclass(BlockDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('block, indent, expected_string', [
    (Block([SimpleStatement([ReturnStatement()])], indent='    '), '', '    return\n'),
    (Block([SimpleStatement([ReturnStatement()])], indent='    '), '    ', '        return\n'),
    (Block([SimpleStatement([ReturnStatement()])], indent='    '), '\t', '\t    return\n'),
    (Block([SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()])], indent='    '), '', '    return\n    return\n'),
    (Block([SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()])], indent='    '), '    ', '        return\n        return\n'),
    (Block([SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()])], indent='    '), '\t', '\t    return\n\t    return\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_block(block: Block, indent: str, expected_string: str) -> None:
    """Test arborista.deparsers.python.block_deparser.BlockDeparser.deparse_block."""
    string: str = BlockDeparser.deparse_block(block, indent)

    assert string == expected_string
