"""A choice between two righthand sides."""
from typing import TYPE_CHECKING, Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

if TYPE_CHECKING:
    from arborista.nodes.nebnf.righthand_side import RighthandSide


class Alternation(NEBNFNode):
    """A choice between two righthand sides."""
    def __init__(self,
                 first_choice: 'RighthandSide',
                 second_choice: 'RighthandSide',
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.first_choice: 'RighthandSide' = first_choice
        self.second_choice: 'RighthandSide' = second_choice

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.first_choice != other.first_choice:
            return False

        if self.second_choice != other.second_choice:
            return False

        return True
