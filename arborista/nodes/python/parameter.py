"""A Python parameter."""
from typing import Any, Iterable, List

from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


class Parameter(PythonNode):  # pylint: disable=too-few-public-methods
    """A Python parameter."""
    def __init__(self, name: Name):
        self.name: Name = name

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Parameter):
            return False
        return self.name == other.name


Parameters = Iterable[Parameter]
ParameterList = List[Parameter]
