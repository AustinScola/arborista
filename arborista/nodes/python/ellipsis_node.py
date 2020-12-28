"""A Python ellipsis."""
from typing import Any

from arborista.nodes.python.atom import Atom


class EllipsisNode(Atom):
    """A Python ellipsis."""
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EllipsisNode):
            return False
        return True
