"""A Python star import target."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type
from arborista.nodes.python.python_node import PythonNode


class Star(PythonNode):
    """A Python star import target."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
