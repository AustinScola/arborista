"""The lefthand side of a production rule."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.nebnf_node import NEBNFNode


class LefthandSide(NEBNFNode):
    """The lefthand side of a production rule."""
    def __init__(self, identifier: Identifier, parent: Optional[Node] = None):
        super().__init__(parent)

        self.identifier: Identifier = identifier
