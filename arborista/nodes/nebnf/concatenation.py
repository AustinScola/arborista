"""A concatenation of two righthand sides."""
from typing import TYPE_CHECKING, Optional

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
