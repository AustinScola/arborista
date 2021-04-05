"""A Python greater than or equals comparison operator."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.nodes.python.comparison_operator import ComparisonOperator


class GreaterThanOrEquals(ComparisonOperator):
    """A Python greater than or equals comparison operator."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
