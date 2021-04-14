"""An optional righthand side."""
from typing import TYPE_CHECKING, Optional

from arborista.node import Node
from arborista.nodes.nebnf.name import Name
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

if TYPE_CHECKING:
    from arborista.nodes.nebnf.righthand_side import RighthandSide  # pragma: no cover


class Option(NEBNFNode):
    """An optional righthand side."""
    def __init__(self,
                 name: Optional[Name],
                 righthand_side: 'RighthandSide',
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Optional[Name] = name
        self.righthand_side: 'RighthandSide' = righthand_side
