"""A Python continue statement."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.nodes.python.flow_statement import FlowStatement


class ContinueStatement(FlowStatement):
    """A Python continue statement."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
