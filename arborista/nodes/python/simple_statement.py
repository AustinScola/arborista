"""A Python simple statement."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node, NodeIterator
from arborista.nodes.python.small_statement import SmallStatementList, SmallStatements
from arborista.nodes.python.statement import Statement


class SimpleStatement(Statement):
    """A Python simple statement."""
    def __init__(self, small_statements: SmallStatements, parent: Optional[Node] = None):
        super().__init__(parent)

        self.small_statements: SmallStatementList = list(small_statements)

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if len(self.small_statements) != len(other.small_statements):
            return False
        return all(small_statement == other_small_statement for small_statement,
                   other_small_statement in zip(self.small_statements, other.small_statements))

    def iterate_children(self) -> NodeIterator:
        yield from self.small_statements
