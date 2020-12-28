"""A Python continue statement."""
from typing import Any

from arborista.nodes.python.flow_statement import FlowStatement


class ContinueStatement(FlowStatement):
    """A Python continue statement."""
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ContinueStatement):
            return False
        return True
