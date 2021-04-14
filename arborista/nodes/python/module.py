"""A Python module."""
from typing import Optional

from arborista.node import Node, NodeIterator
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.statement import StatementList, Statements


class Module(PythonNode):
    """A Python module."""
    def __init__(self,
                 name: str,
                 statements: Optional[Statements] = None,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: str = name

        self.statements: StatementList
        if statements is None:
            self.statements = []
        else:
            self.statements = list(statements)

    def iterate_children(self) -> NodeIterator:
        yield from self.statements
