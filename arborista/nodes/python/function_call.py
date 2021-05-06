"""A Python function call."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.expression import Expression


class FunctionCall(Expression):
    """A Python function call."""
    def __init__(self,
                 function: Expression,
                 arguments: Optional[Arguments] = None,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.function: Expression = function
        self.arguments: Arguments = Arguments() if arguments is None else arguments
