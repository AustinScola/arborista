"""A Python module."""
from typing import List

from arborista.node import Node
from arborista.nodes.python.statement import Statement, Statements


class Module(Node):  # pylint: disable=too-few-public-methods
    """A Python module."""
    def __init__(self, name: str, statements: Statements):
        self.name: str = name
        self.statements: List[Statement] = list(statements)
