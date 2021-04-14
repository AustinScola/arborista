"""A production rule."""
from typing import TYPE_CHECKING, Optional

from arborista.node import Node
from arborista.nodes.nebnf.lefthand_side import LefthandSide
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

if TYPE_CHECKING:
    from arborista.nodes.nebnf.righthand_side import RighthandSide  # pragma: no cover


class Rule(NEBNFNode):
    """A production rule."""
    def __init__(self,
                 lefthand_side: LefthandSide,
                 righthand_side: 'RighthandSide',
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.lefthand_side: LefthandSide = lefthand_side
        self.righthand_side: 'RighthandSide' = righthand_side
