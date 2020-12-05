"""A Python simple statement."""
from typing import Any

from arborista.nodes.python.small_statement import SmallStatementList, SmallStatements
from arborista.nodes.python.statement import Statement


class SimpleStatement(Statement):
    """A Python simple statement."""
    def __init__(self, small_statements: SmallStatements):
        self.small_statements: SmallStatementList = list(small_statements)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SimpleStatement):
            return False
        if len(self.small_statements) != len(other.small_statements):
            return False
        return all(small_statement == other_small_statement for small_statement,
                   other_small_statement in zip(self.small_statements, other.small_statements))
