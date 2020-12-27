"""A Python pass statement."""
from typing import Any

from arborista.nodes.python.small_statement import SmallStatement


class PassStatement(SmallStatement):
    """A Python pass statement."""
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, PassStatement):
            return False
        return True
