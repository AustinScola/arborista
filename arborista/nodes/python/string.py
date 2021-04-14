"""A Python string."""
from typing import Optional, Union

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
