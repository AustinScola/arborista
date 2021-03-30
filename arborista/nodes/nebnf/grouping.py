"""An grouping righthand side."""
from typing import TYPE_CHECKING, Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.nebnf.name import Name
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

if TYPE_CHECKING:
    from arborista.nodes.nebnf.righthand_side import RighthandSide  # pragma: no cover


class Grouping(NEBNFNode):
    """An grouping righthand side."""
    def __init__(self,
                 name: Optional[Name],
                 righthand_side: 'RighthandSide',
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.name: Optional[Name] = name
        self.righthand_side: 'RighthandSide' = righthand_side

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.name != other.name:
            return False

        if self.righthand_side != other.righthand_side:
            return False

        return True
