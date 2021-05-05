"""Deparser for a Python block."""
from arborista.deparser import Deparser
from arborista.nodes.python.block import Block


class BlockDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python block."""
    @staticmethod
    def deparse_block(block: Block, indent: str) -> str:
        """Deparse a Python block."""
        from arborista.deparsers.python.statement_deparser import StatementDeparser  # isort: skip # pylint: disable=import-outside-toplevel
        string: str = ''

        for statement in block.body:
            statement_string: str = StatementDeparser.deparse_statement(
                statement, indent + block.indent)
            string += statement_string

        return string
