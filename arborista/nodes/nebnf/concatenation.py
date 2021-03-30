"""A concatenation of two righthand sides."""
from typing import TYPE_CHECKING, Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

if TYPE_CHECKING:
    from arborista.nodes.nebnf.righthand_side import RighthandSide  # pragma: no cover


class Concatenation(NEBNFNode):
    """A concatenation of two righthand sides."""
    def __init__(self,
                 first: 'RighthandSide',
                 second: 'RighthandSide',
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.first: 'RighthandSide' = first
        self.second: 'RighthandSide' = second

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.first != other.first:
            return False

        if self.second != other.second:
            return False

        return True
