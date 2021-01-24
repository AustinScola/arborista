"""A Python ellipsis."""
from typing import Any

from arborista.decorators.equality.equal_type import equal_type
from arborista.nodes.python.atom import Atom


class EllipsisNode(Atom):
    """A Python ellipsis."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
