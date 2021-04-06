"""A Python in comparison operator."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.nodes.python.comparison_operator import ComparisonOperator


class In(ComparisonOperator):
    """A Python in comparison operator."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
