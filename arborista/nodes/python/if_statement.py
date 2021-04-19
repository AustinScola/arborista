"""A Python if statement."""
from typing import List, Optional

from arborista.node import Node
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.elif_ import Elif, Elifs
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.if_ import If


class IfStatement(CompoundStatement):
    """A Python if statement."""
    def __init__(self, if_: If, elifs: Elifs, else_: Optional[Else], parent: Optional[Node] = None):
        super().__init__(parent)

        self.if_: If = if_
        self.elifs: List[Elif] = list(elifs)
        self.else_: Optional[Else] = else_
