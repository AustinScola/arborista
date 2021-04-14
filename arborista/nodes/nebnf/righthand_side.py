"""The righthand side of a production rule."""
from typing import Optional, Union

from arborista.node import Node
from arborista.nodes.nebnf.alternation import Alternation
from arborista.nodes.nebnf.concatenation import Concatenation
from arborista.nodes.nebnf.grouping import Grouping
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.option import Option
from arborista.nodes.nebnf.repetition import Repetition
from arborista.nodes.nebnf.terminal import Terminal

Expression = Union[Terminal, Identifier, Option, Grouping, Repetition, Alternation, Concatenation]


class RighthandSide(NEBNFNode):
    """The righthand side of a production rule."""
    def __init__(self, expression: Expression, parent: Optional[Node] = None):
        super().__init__(parent)

        self.expression: Expression = expression
