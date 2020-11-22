"""A Python module."""
from typing import Any, Optional

from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.statement import StatementList, Statements


class Module(PythonNode):  # pylint: disable=too-few-public-methods
    """A Python module."""
    def __init__(self, name: str, statements: Optional[Statements] = None):
        self.name: str = name

        self.statements: StatementList
        if statements is None:
            self.statements = []
        else:
            self.statements = list(statements)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Module):
            return False

        if self.name != other.name:
            return False

        if self.statements != other.statements:
            return False

        return True
