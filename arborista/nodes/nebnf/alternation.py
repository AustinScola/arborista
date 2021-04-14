"""A choice between two righthand sides."""
from typing import TYPE_CHECKING, Optional

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

if TYPE_CHECKING:
    from arborista.nodes.nebnf.righthand_side import RighthandSide  # pragma: no cover


class Alternation(NEBNFNode):
    """A choice between two righthand sides."""
    def __init__(self,
                 first_choice: 'RighthandSide',
                 second_choice: 'RighthandSide',
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.first_choice: 'RighthandSide' = first_choice
        self.second_choice: 'RighthandSide' = second_choice
