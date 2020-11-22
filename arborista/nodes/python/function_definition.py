"""A Python function defintion."""
from typing import Any

from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import ParameterList, Parameters
from arborista.nodes.python.statement import StatementList, Statements


class FunctionDefinition(CompoundStatement):  # pylint: disable=too-few-public-methods
    """A Python function defintion."""
    def __init__(self, name: Name, parameters: Parameters, body: Statements):
        self.name: Name = name
        self.parameters: ParameterList = list(parameters)
        self.body: StatementList = list(body)

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
