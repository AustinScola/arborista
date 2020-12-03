"""A Python block."""
from typing import Any

from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.statement import StatementList, Statements


class Block(PythonNode):  # pylint: disable=too-few-public-methods
    """A Python block."""
    def __init__(self, statements: Statements):
        self.body: StatementList = list(statements)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Block):
            return False

        return self.body == other.body
