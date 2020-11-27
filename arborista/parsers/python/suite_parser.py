"""Parser for a Python suite."""
from typing import cast

import libcst

from arborista.nodes.python.block import Block
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite
from arborista.parser import Parser
from arborista.parsers.python.block_parser import BlockParser, LibcstBlock
from arborista.parsers.python.simple_statement_parser import (LibcstSimpleStatement,
                                                              SimpleStatementParser)

LibcstSuite = libcst.BaseSuite


class SuiteParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python suite."""
    @staticmethod
    def parse_suite(libcst_suite: LibcstSuite) -> Suite:
        """Parser a Python suite."""
        suite: Suite
        if isinstance(libcst_suite, libcst.SimpleStatementSuite):
            libcst_simple_statement: LibcstSimpleStatement = libcst_suite
            simple_statement: SimpleStatement = SimpleStatementParser.parse_simple_statement(
                libcst_simple_statement)
            suite = simple_statement
        else:
            libcst_block: LibcstBlock = cast(LibcstBlock, libcst_suite)
            block: Block = BlockParser.parse_block(libcst_block)
            suite = block
        return suite
