"""Test arborista.nodes.python.function_definition."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.block import Block
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.decorator import Decorator, DecoratorList
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.positional_parameter import PositionalParameter
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite


def test_inheritance() -> None:
    """Test arborista.nodes.python.function_definition.FunctionDefinition inheritance."""
    assert issubclass(FunctionDefinition, CompoundStatement)


_PARENT = MagicMock()


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, keyword_arguments, expected_name, expected_parameters, expected_body, expected_decorators, expected_returns, expected_parent', [
    ([Name('f'), Parameters(), SimpleStatement([ReturnStatement()])], {}, Name('f'), Parameters(), SimpleStatement([ReturnStatement()]), [], None, None),
    ([Name('f'), Parameters(), SimpleStatement([ReturnStatement()])], {'parent': None}, Name('f'), Parameters(), SimpleStatement([ReturnStatement()]), [], None, None),
    ([Name('f'), Parameters(), SimpleStatement([ReturnStatement()])], {'parent': _PARENT}, Name('f'), Parameters(), SimpleStatement([ReturnStatement()]), [], None, _PARENT),
    ([Name('f'), Parameters(), SimpleStatement([ReturnStatement()])], {'decorators': [Decorator(DottedName(Name('d'), []))]}, Name('f'), Parameters(), SimpleStatement([ReturnStatement()]), [Decorator(DottedName(Name('d'), []))], None, None),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_function_definition_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
                                  expected_name: Name, expected_parameters: Parameters,
                                  expected_body: Suite, expected_decorators: DecoratorList,
                                  expected_returns: Optional[Expression],
                                  expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.function_definition.__init__."""
    function_definition: FunctionDefinition = FunctionDefinition(*arguments, **keyword_arguments)

    assert function_definition.name == expected_name
    assert function_definition.parameters == expected_parameters
    assert function_definition.body == expected_body
    assert function_definition.decorators == expected_decorators
    assert function_definition.returns == expected_returns
    assert function_definition.parent is expected_parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('function_definition, expected_children_list', [
    (FunctionDefinition(Name('foo'), Parameters(), SimpleStatement([ReturnStatement()])), [Name('foo'), Parameters(), SimpleStatement([ReturnStatement()])]),
    (FunctionDefinition(Name('foo'), Parameters(), SimpleStatement([ReturnStatement()]), returns=Name('Bar')), [Name('foo'), Parameters(), SimpleStatement([ReturnStatement()]), Name('Bar')]),
    (FunctionDefinition(Name('foo'), Parameters(), SimpleStatement([ReturnStatement()]), [Decorator(DottedName(Name('d'), []))]), [Name('foo'), Parameters(), SimpleStatement([ReturnStatement()]), Decorator(DottedName(Name('d'), []))]),
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
