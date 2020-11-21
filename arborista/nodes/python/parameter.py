"""A Python parameter."""
from typing import Iterable, List

from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


class Parameter(PythonNode):  # pylint: disable=too-few-public-methods
    """A Python parameter."""
    def __init__(self, name: Name):
        self.name: Name = name


Parameters = Iterable[Parameter]
ParameterList = List[Parameter]
