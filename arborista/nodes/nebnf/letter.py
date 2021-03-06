"""A letter."""
from typing import Any, Optional, Union

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.nebnf.lowercase_letter import LowercaseLetterValue
from arborista.nodes.nebnf.nebnf_node import NEBNFNode
from arborista.nodes.nebnf.uppercase_letter import UppercaseLetterValue

LetterValue = Union[LowercaseLetterValue, UppercaseLetterValue]


class Letter(NEBNFNode):
    """A letter."""
    def __init__(self, value: LetterValue, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: LetterValue = value

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value
        return equality
