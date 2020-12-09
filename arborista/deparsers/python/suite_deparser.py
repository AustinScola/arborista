"""Deparser for a Python suite."""
from arborista.deparser import Deparser
from arborista.deparsers.python.block_deparser import BlockDeparser
from arborista.deparsers.python.simple_statement_deparser import SimpleStatementDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite


class SuiteDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python suite."""
    @staticmethod
    def deparse_suite(suite: Suite, indent: str) -> str:
        """Deparse a Python suite."""
        string: str
        if isinstance(suite, SimpleStatement):
            simple_statement: SimpleStatement = suite
            simple_statement_string: str = SimpleStatementDeparser.deparse_simple_statement(
                simple_statement, indent)
            string = simple_statement_string
        else:
            block: Block = suite
            block_string: str = BlockDeparser.deparse_block(block, indent)
            string = block_string
        return string
