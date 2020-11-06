"""A Python parameter."""
from typing import Iterable, List

from arborista.nodes.python.statement import Statement


class Parameter(Statement):  # pylint: disable=too-few-public-methods
    """A Python parameter."""


Parameters = Iterable[Parameter]
ParameterList = List[Parameter]
