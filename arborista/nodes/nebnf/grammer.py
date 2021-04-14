"""An NEBNF grammer."""
from typing import List, Optional

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.rule import Rule


class Grammer(NEBNFNode):
    """An NEBNF grammer."""
    def __init__(self, rules: List[Rule], parent: Optional[Node] = None):
        super().__init__(parent)

        self.rules: List[Rule] = rules
