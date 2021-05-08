"""A Python keyword argument."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.argument import Argument
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.name import Name


class KeywordArgument(Argument):
    """A Python keyword argument."""
    def __init__(self, name: Name, value: Expression, parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Name = name
        self.value: Expression = value
