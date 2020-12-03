"""Parser for a Python block."""
import libcst

from arborista.nodes.python.block import Block
from arborista.nodes.python.statement import StatementList
from arborista.parser import Parser
from arborista.parsers.python.statement_parser import LibcstStatements

LibcstBlock = libcst.IndentedBlock


class BlockParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python block."""
    @staticmethod
    def parse_block(libcst_block: LibcstBlock) -> Block:
        """Parser a Python block."""

        from arborista.parsers.python.statement_parser import StatementParser  # isort: skip  # pylint: disable=cyclic-import, import-outside-toplevel

        libcst_body: LibcstStatements = libcst_block.body
        statements: StatementList = [
            StatementParser.parse_statement(libcst_statement) for libcst_statement in libcst_body
        ]

        block: Block = Block(statements)
        return block
