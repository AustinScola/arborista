"""A Python simple statement."""
from typing import Optional

from arborista.node import Node, NodeIterator
from arborista.nodes.python.small_statement import SmallStatementList, SmallStatements
from arborista.nodes.python.statement import Statement


class SimpleStatement(Statement):
    """A Python simple statement."""
    def __init__(self, small_statements: SmallStatements, parent: Optional[Node] = None):
        super().__init__(parent)

        self.small_statements: SmallStatementList = list(small_statements)

    def iterate_children(self) -> NodeIterator:
        yield from self.small_statements
