"""Parser for a Python block."""
from typing import Optional

import libcst

from arborista.nodes.python.block import Block
from arborista.nodes.python.statement import StatementIterator
from arborista.parser import Parser

LibcstBlock = libcst.IndentedBlock


class BlockParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python block."""
    @staticmethod
    def parse_block(libcst_block: LibcstBlock) -> Block:
        """Parser a Python block."""

        from arborista.parsers.python.statement_parser import StatementParser, LibcstStatements  # isort: skip  # pylint: disable=cyclic-import, import-outside-toplevel, line-too-long, useless-suppression

        libcst_body: LibcstStatements = libcst_block.body
        body: StatementIterator = (StatementParser.parse_statement(libcst_statement)
                                   for libcst_statement in libcst_body)

        indent: str
        libcst_indent: Optional[str] = libcst_block.indent
        if libcst_indent is None:
            indent = '    '
        else:
            indent = libcst_indent

        block: Block = Block(body, indent)
        block.set_parent_in_children()

        return block
