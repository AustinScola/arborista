"""A Python is not comparison operator."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.nodes.python.comparison_operator import ComparisonOperator


class IsNot(ComparisonOperator):
    """A Python is not comparison operator."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
