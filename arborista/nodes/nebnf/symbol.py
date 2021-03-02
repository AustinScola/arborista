"""A symbol."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type
from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

SymbolValue = Literal['[', ']', '{', '}', '(', '}', '<', '>', "'", '"', '=', '|', '.', ';']


class Symbol(NEBNFNode):
    """A symbol."""
    def __init__(self, value: SymbolValue, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: SymbolValue = value

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value
        return equality
