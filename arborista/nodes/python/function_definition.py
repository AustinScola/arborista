"""A Python function defintion."""
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import ParameterList, Parameters
from arborista.nodes.python.statement import Statement, StatementList, Statements


class FunctionDefinition(Statement):  # pylint: disable=too-few-public-methods
    """A Python function defintion."""
    def __init__(self, name: Name, parameters: Parameters, body: Statements):
        self.name: Name = name
        self.parameters: ParameterList = list(parameters)
        self.body: StatementList = list(body)
