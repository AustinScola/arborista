"""An NEBNF grammer."""
from typing import Any, List, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.rule import Rule


class Grammer(NEBNFNode):
    """An NEBNF grammer."""
    def __init__(self, rules: List[Rule], parent: Optional[Node] = None):
        super().__init__(parent)

        self.rules: List[Rule] = rules

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.rules != other.rules:
            return False

        return True
