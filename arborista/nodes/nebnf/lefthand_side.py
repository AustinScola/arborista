"""The lefthand side of a production rule."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.nebnf.identifier import Identifier
from arborista.nodes.nebnf.nebnf_node import NEBNFNode


class LefthandSide(NEBNFNode):
    """The lefthand side of a production rule."""
    def __init__(self, identifier: Identifier, parent: Optional[Node] = None):
        super().__init__(parent)

        self.identifier: Identifier = identifier

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.identifier == other.identifier
        return equality
