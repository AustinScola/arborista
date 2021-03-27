"""An optional righthand side."""
from typing import TYPE_CHECKING, Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

if TYPE_CHECKING:
    from arborista.nodes.nebnf.righthand_side import RighthandSide


class Option(NEBNFNode):
    """An optional righthand side."""
    def __init__(self, righthand_side: 'RighthandSide', parent: Optional[Node] = None):
        super().__init__(parent)

        self.righthand_side: 'RighthandSide' = righthand_side

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.righthand_side != other.righthand_side:
            return False

        return True
