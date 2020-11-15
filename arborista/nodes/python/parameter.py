"""A Python parameter."""
from typing import Iterable, List

from arborista.nodes.python.python_node import PythonNode


class Parameter(PythonNode):  # pylint: disable=too-few-public-methods
    """A Python parameter."""


Parameters = Iterable[Parameter]
ParameterList = List[Parameter]
