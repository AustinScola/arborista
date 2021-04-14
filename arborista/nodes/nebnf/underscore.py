"""An underscore."""
from typing import Optional

from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

UnderscoreValue = Literal['_']


class Underscore(NEBNFNode):
    """A underscore."""
    def __init__(self, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: UnderscoreValue = '_'
