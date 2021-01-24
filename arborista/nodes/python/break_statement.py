"""A Python break statement."""
from typing import Any

from arborista.decorators.equality.equal_type import equal_type
from arborista.nodes.python.flow_statement import FlowStatement


class BreakStatement(FlowStatement):
    """A Python break statement."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
