"""A symbol."""
from typing import Optional

from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

SymbolValue = Literal['[', ']', '{', '}', '(', '}', '<', '>', "'", '"', '=', '|', '.', ';']


class Symbol(NEBNFNode):
    """A symbol."""
    def __init__(self, value: SymbolValue, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: SymbolValue = value
