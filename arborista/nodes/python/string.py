"""A Python string."""
from typing import Any, Optional, Union

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.long_string import LongString
from arborista.nodes.python.short_string import ShortString
from arborista.nodes.python.string_prefix import StringPrefix

StringValue = Union[ShortString, LongString]


class String(Atom):
    """A Python string."""
    def __init__(self,
                 prefix: Optional[StringPrefix],
                 value: StringValue,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.prefix: Optional[StringPrefix] = prefix
        self.value: StringValue = value

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.prefix != other.prefix:
            return False

        if self.value != other.value:
            return False

        return True
