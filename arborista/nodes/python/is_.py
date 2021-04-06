"""A Python is comparison operator."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.nodes.python.comparison_operator import ComparisonOperator


class Is(ComparisonOperator):
    """A Python is comparison operator."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
