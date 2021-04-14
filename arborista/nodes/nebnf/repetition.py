"""A repetition of righthand sides."""
from typing import TYPE_CHECKING, Optional

from arborista.node import Node
from arborista.nodes.nebnf.name import Name
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

if TYPE_CHECKING:
    from arborista.nodes.nebnf.righthand_side import RighthandSide  # pragma: no cover


class Repetition(NEBNFNode):
    """A repetition of righthand sides."""
    def __init__(self,
                 name: Optional[Name],
                 element: 'RighthandSide',
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Optional[Name] = name
        self.element: 'RighthandSide' = element
