"""A Python block."""
from typing import Optional

from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.statement import Statement, StatementList, Statements


class Block(PythonNode):  # pylint: disable=too-few-public-methods
    """A Python block."""
    def __init__(self, first_statement: Statement, rest_of_statements: Optional[Statements] = None):
        self.body: StatementList = [first_statement]
        if rest_of_statements is not None:
            self.body += list(rest_of_statements)
