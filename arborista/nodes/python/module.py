"""A Python module."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.statement import StatementList, Statements


class Module(Node):  # pylint: disable=too-few-public-methods
    """A Python module."""
    def __init__(self, name: str, statements: Optional[Statements] = None):
        self.name: str = name

        self.statements: StatementList
        if statements is None:
            self.statements = []
        else:
            self.statements = list(statements)
