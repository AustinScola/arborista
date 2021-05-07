"""A Python simple statement."""
from typing import Optional

from arborista.node import Node, NodeIterator
from arborista.nodes.python.small_statement import SmallStatementList, SmallStatements
from arborista.nodes.python.statement import Statement
from arborista.nodes.python.trailing_whitespace import TrailingWhitespace


class SimpleStatement(Statement):
    """A Python simple statement."""
    def __init__(self,
                 small_statements: SmallStatements,
                 trailing_whitespace: Optional[TrailingWhitespace] = None,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.small_statements: SmallStatementList = list(small_statements)
        self.trailing_whitespace: TrailingWhitespace = TrailingWhitespace(
        ) if trailing_whitespace is None else trailing_whitespace

    def iterate_children(self) -> NodeIterator:
        yield from self.small_statements
