"""A Python joined string."""
from typing import Any, Iterable, Iterator, List, Optional, Union

from arborista.decorators.equality.equal_type import equal_type
from arborista.node import Node
from arborista.nodes.python.formatted_string import FormattedString
from arborista.nodes.python.simple_string import SimpleString
from arborista.nodes.python.string import String


class JoinedString(String):
    """A Python joined string."""
    def __init__(self,
                 strings: Iterable[Union[SimpleString, FormattedString]],
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.strings: List[Union[SimpleString, FormattedString]] = list(strings)

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.strings != other.strings:
            return False

        return True

    def iterate_children(self) -> Iterator[Union[SimpleString, FormattedString]]:
        yield from self.strings
