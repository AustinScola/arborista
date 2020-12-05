"""A Python return statement."""
from typing import Any

from arborista.nodes.python.flow_statement import FlowStatement


class ReturnStatement(FlowStatement):
    """A Python return statement."""
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ReturnStatement):
            return False
        return True
