"""A Python break statement."""
from typing import Any

from arborista.nodes.python.flow_statement import FlowStatement


class BreakStatement(FlowStatement):
    """A Python break statement."""
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, BreakStatement):
            return False
        return True
