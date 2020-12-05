"""A Python block."""
from typing import Any

from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.statement import StatementList, Statements


class Block(PythonNode):
    """A Python block."""
    def __init__(self, body: Statements, indent: str):
        self.body: StatementList = list(body)
        self.indent: str = indent

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Block):
            return False

        return self.body == other.body
