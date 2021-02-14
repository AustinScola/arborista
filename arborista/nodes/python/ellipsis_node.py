"""A Python ellipsis."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.nodes.python.atom import Atom


class EllipsisNode(Atom):
    """A Python ellipsis."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
