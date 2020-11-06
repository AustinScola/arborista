"""A Python simple statement."""
from arborista.nodes.python.small_statement import SmallStatements
from arborista.nodes.python.statement import Statement


class SimpleStatement(Statement):  # pylint: disable=too-few-public-methods
    """A Python simple statement."""
    def __init__(self, small_statements: SmallStatements):
        self.small_statements: SmallStatements = small_statements
