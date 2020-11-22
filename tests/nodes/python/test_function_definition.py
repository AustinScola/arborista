"""Test arborista.nodes.python.function_definition."""
from typing import Any

import pytest

from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import Parameter, ParameterList, Parameters
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.statement import StatementList, Statements


def test_inheritance() -> None:
    """Test arborista.nodes.python.function_definition.FunctionDefinition inheritance."""
    assert issubclass(FunctionDefinition, CompoundStatement)


# yapf: disable
@pytest.mark.parametrize('name, parameters, body, expected_parameters, expected_body', [
    (Name('f'), [], [], [], []),
    (Name('f'), [], iter([]), [], []),
    (Name('f'), iter([]), [], [], []),
    (Name('f'), iter([]), iter([]), [], []),
])
# yapf: enable
def test_function_definition_init(name: Name, parameters: Parameters, body: Statements,
                                  expected_parameters: ParameterList,
                                  expected_body: StatementList) -> None:
    """Test arborista.nodes.python.function_definition.__init__."""
    function_definition: FunctionDefinition = FunctionDefinition(name, parameters, body)

    assert function_definition.name == name
    assert function_definition.parameters == expected_parameters
    assert function_definition.body == expected_body


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('function_definition, other, expected_equality', [
    (FunctionDefinition(Name('foo'), [], []), 'bar', False),
    (FunctionDefinition(Name('foo'), [], []), FunctionDefinition(Name('bar'), [], []), False),
    (FunctionDefinition(Name('foo'), [Parameter(Name('x'))], []), FunctionDefinition(Name('foo'), [], []), False),
    (FunctionDefinition(Name('foo'), [], [SimpleStatement([ReturnStatement()])]), FunctionDefinition(Name('foo'), [], []), False),
    (FunctionDefinition(Name('foo'), [], []), FunctionDefinition(Name('foo'), [], []), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(function_definition: FunctionDefinition, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.function_definition.__eq__."""
    equality: bool = function_definition == other
    assert equality == expected_equality
