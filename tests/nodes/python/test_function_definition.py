"""Test arborista.nodes.python.function_definition."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.block import Block
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.module import Module
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import Parameter, ParameterList, Parameters
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite


def test_inheritance() -> None:
    """Test arborista.nodes.python.function_definition.FunctionDefinition inheritance."""
    assert issubclass(FunctionDefinition, CompoundStatement)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('name, parameters, body, parent, pass_parent, expected_parameters', [
    (Name('f'), [], ReturnStatement(), None, False, []),
    (Name('f'), [], ReturnStatement(), None, True, []),
    (Name('f'), [], ReturnStatement(), Module('foo'), True, []),
    (Name('f'), [], Block([SimpleStatement([ReturnStatement()])], '    '), None, False, []),
    (Name('f'), [], Block([SimpleStatement([ReturnStatement()])], '    '), None, True, []),
    (Name('f'), [], Block([SimpleStatement([ReturnStatement()])], '    '), Module('foo'), True, []),
    (Name('f'), iter([]), ReturnStatement(), None, False, []),
    (Name('f'), iter([]), ReturnStatement(), None, True, []),
    (Name('f'), iter([]), ReturnStatement(), Module('foo'), True, []),
    (Name('f'), iter([]), Block([SimpleStatement([ReturnStatement()])], '    '), None, False, []),
    (Name('f'), iter([]), Block([SimpleStatement([ReturnStatement()])], '    '), None, True, []),
    (Name('f'), iter([]), Block([SimpleStatement([ReturnStatement()])], '    '), Module('foo'), True, []),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_function_definition_init(name: Name, parameters: Parameters, body: Suite,
                                  parent: Optional[Node], pass_parent: bool,
                                  expected_parameters: ParameterList) -> None:
    """Test arborista.nodes.python.function_definition.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    function_definition: FunctionDefinition = FunctionDefinition(name, parameters, body,
                                                                 **keyword_arguments)

    assert function_definition.name == name
    assert function_definition.parameters == expected_parameters
    assert function_definition.body == body
    assert id(function_definition.parent) == id(parent)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('function_definition, expected_children_list', [
    (FunctionDefinition(Name('foo'), [], SimpleStatement([ReturnStatement()])), [Name('foo'), SimpleStatement([ReturnStatement()])]),
    (FunctionDefinition(Name('foo'), [], Block([SimpleStatement([ReturnStatement()])], '    ')), [Name('foo'), Block([SimpleStatement([ReturnStatement()])], '    ')]),
    (FunctionDefinition(Name('foo'), [Parameter(Name('x'))], SimpleStatement([ReturnStatement()])), [Name('foo'), Parameter(Name('x')), SimpleStatement([ReturnStatement()])]),
    (FunctionDefinition(Name('foo'), [Parameter(Name('x'))], SimpleStatement([ReturnStatement()])), [Name('foo'), Parameter(Name('x')), SimpleStatement([ReturnStatement()])]),
    (FunctionDefinition(Name('foo'), [Parameter(Name('x')), Parameter(Name('y')), Parameter(Name('z'))], SimpleStatement([ReturnStatement()])), [Name('foo'), Parameter(Name('x')), Parameter(Name('y')), Parameter(Name('z')), SimpleStatement([ReturnStatement()])]),
])
# yapf: enable # pylint: enable=line-too-long
def test_iterate_children(function_definition: FunctionDefinition,
                          expected_children_list: NodeList) -> None:
    """Test arborista.nodes.python.function_definition.iterate_children."""
    children: NodeIterator = function_definition.iterate_children()
    children_list: NodeList = list(children)

    assert children_list == expected_children_list
