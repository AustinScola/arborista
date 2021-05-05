"""Test arborista.nodes.python.function_definition."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.block import Block
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.module import Module
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.positional_parameter import PositionalParameter, PositionalParameterList
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite


def test_inheritance() -> None:
    """Test arborista.nodes.python.function_definition.FunctionDefinition inheritance."""
    assert issubclass(FunctionDefinition, CompoundStatement)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('name, parameters, body, returns, parent, pass_parent, expected_parameters', [
    (Name('f'), Parameters(), ReturnStatement(), None, None, False, Parameters()),
    (Name('f'), Parameters(), ReturnStatement(), None, None, True, Parameters()),
    (Name('f'), Parameters(), ReturnStatement(), None, Module('foo'), True, Parameters()),
    (Name('f'), Parameters(), Block([SimpleStatement([ReturnStatement()])], '    '), None, None, False, Parameters()),
    (Name('f'), Parameters(), Block([SimpleStatement([ReturnStatement()])], '    '), None, None, True, Parameters()),
    (Name('f'), Parameters(), Block([SimpleStatement([ReturnStatement()])], '    '), None, Module('foo'), True, Parameters()),
    (Name('f'), Parameters(), ReturnStatement(), None, None, False, Parameters()),
    (Name('f'), Parameters(), ReturnStatement(), None, None, True, Parameters()),
    (Name('f'), Parameters(), ReturnStatement(), None, Module('foo'), True, Parameters()),
    (Name('f'), Parameters(), Block([SimpleStatement([ReturnStatement()])], '    '), None, None, False, Parameters()),
    (Name('f'), Parameters(), Block([SimpleStatement([ReturnStatement()])], '    '), None, None, True, Parameters()),
    (Name('f'), Parameters(), Block([SimpleStatement([ReturnStatement()])], '    '), None, Module('foo'), True, Parameters()),
    (Name('f'), Parameters(), ReturnStatement(), Name('Foo'), None, False, Parameters()),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_function_definition_init(name: Name, parameters: Parameters, body: Suite,
                                  returns: Expression, parent: Optional[Node], pass_parent: bool,
                                  expected_parameters: PositionalParameterList) -> None:
    """Test arborista.nodes.python.function_definition.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    function_definition: FunctionDefinition = FunctionDefinition(name, parameters, body, returns,
                                                                 **keyword_arguments)

    assert function_definition.name == name
    assert function_definition.parameters == expected_parameters
    assert function_definition.body == body
    assert function_definition.returns == returns
    assert id(function_definition.parent) == id(parent)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('function_definition, expected_children_list', [
    (FunctionDefinition(Name('foo'), Parameters(), SimpleStatement([ReturnStatement()])), [Name('foo'), Parameters(), SimpleStatement([ReturnStatement()])]),
    (FunctionDefinition(Name('foo'), Parameters(), SimpleStatement([ReturnStatement()]), Name('Bar')), [Name('foo'), Parameters(), SimpleStatement([ReturnStatement()]), Name('Bar')]),
    (FunctionDefinition(Name('foo'), Parameters(), Block([SimpleStatement([ReturnStatement()])], '    ')), [Name('foo'), Parameters(), Block([SimpleStatement([ReturnStatement()])], '    ')]),
    (FunctionDefinition(Name('foo'), Parameters([PositionalParameter(Name('x'))]), SimpleStatement([ReturnStatement()])), [Name('foo'), Parameters([PositionalParameter(Name('x'))]), SimpleStatement([ReturnStatement()])]),
    (FunctionDefinition(Name('foo'), Parameters([PositionalParameter(Name('x')), PositionalParameter(Name('y')), PositionalParameter(Name('z'))]), SimpleStatement([ReturnStatement()])), [Name('foo'), Parameters([PositionalParameter(Name('x')), PositionalParameter(Name('y')), PositionalParameter(Name('z'))]), SimpleStatement([ReturnStatement()])]),
])
# yapf: enable # pylint: enable=line-too-long
def test_iterate_children(function_definition: FunctionDefinition,
                          expected_children_list: NodeList) -> None:
    """Test arborista.nodes.python.function_definition.iterate_children."""
    children: NodeIterator = function_definition.iterate_children()
    children_list: NodeList = list(children)

    assert children_list == expected_children_list
