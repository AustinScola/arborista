"""The righthand side of a production rule."""
from typing import Any, Optional, Union

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.option import Option
from arborista.nodes.nebnf.grouping import Grouping
from arborista.nodes.nebnf.terminal import Terminal

Expression = Union[Terminal, Identifier, Option, Grouping]


class RighthandSide(NEBNFNode):
    """The righthand side of a production rule."""
    def __init__(self, expression: Expression, parent: Optional[Node] = None):
        super().__init__(parent)

        self.expression: Expression = expression

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.expression == other.expression
        return equality
