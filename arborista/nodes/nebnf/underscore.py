"""An underscore."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type
from typing_extensions import Literal

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode

UnderscoreValue = Literal['_']


class Underscore(NEBNFNode):
    """A underscore."""
    def __init__(self, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: UnderscoreValue = '_'

    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
