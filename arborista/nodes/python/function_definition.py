"""A Python function defintion."""
from typing import Any

from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import ParameterList, Parameters
from arborista.nodes.python.suite import Suite


class FunctionDefinition(CompoundStatement):
    """A Python function defintion."""
    def __init__(self, name: Name, parameters: Parameters, body: Suite):
        self.name: Name = name
        self.parameters: ParameterList = list(parameters)
        self.body: Suite = body

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, FunctionDefinition):
            return False

        if self.name != other.name:
            return False

        if self.parameters != other.parameters:
            return False

        if self.body != other.body:
            return False

        return True
