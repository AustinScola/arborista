"""A Python for statement."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.expression_list import ExpressionList
from arborista.nodes.python.suite import Suite


class ForStatement(CompoundStatement):
    """A Python for statement."""

    # pylint: disable=too-many-arguments
    def __init__(self,
                 values: ExpressionList,
                 sources: ExpressionList,
                 body: Suite,
                 else_: Optional[Else],
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.values: ExpressionList = values
        self.sources: ExpressionList = sources
        self.body: Suite = body
        self.else_: Optional[Else] = else_
