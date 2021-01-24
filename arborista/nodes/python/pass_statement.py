"""A Python pass statement."""
from typing import Any

from arborista.decorators.equality.equal_type import equal_type
from arborista.nodes.python.small_statement import SmallStatement


class PassStatement(SmallStatement):
    """A Python pass statement."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
