"""A Python return statement."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.nodes.python.flow_statement import FlowStatement


class ReturnStatement(FlowStatement):
    """A Python return statement."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
