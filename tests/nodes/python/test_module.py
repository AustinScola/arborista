"""Test arborista.nodes.python.module."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.module import Module
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.statement import StatementList, Statements
from testing_helpers.animal_nodes import Lizard


def test_inheritance() -> None:
    """Test arborista.nodes.python.module.Module inheritance."""
    assert issubclass(Module, PythonNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('name, statements, pass_statements, parent, pass_parent, expected_statements', [
    ('foo', [], True, None, False, []),
    ('foo', [], True, None, True, []),
    ('foo', [], True, Lizard(), True, []),
    ('foo', iter([]), True, None, False, []),
    ('foo', iter([]), True, None, True, []),
    ('foo', iter([]), True, Lizard(), True, []),
    ('foo', None, False, None, False, []),
    ('foo', None, False, None, True, []),
    ('foo', None, False, Lizard(), True, []),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_module_init(name: str, statements: Optional[Statements], pass_statements: bool,
                     parent: Optional[Node], pass_parent: bool,
                     expected_statements: StatementList) -> None:
    """Test arborista.nodes.python.module.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_statements:
        keyword_arguments['statements'] = statements
    if pass_parent:
        keyword_arguments['parent'] = parent

    module: Module = Module(name, **keyword_arguments)

    assert module.name == name
    assert module.statements == expected_statements
    assert id(module.parent) == id(parent)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('module, expected_children_list', [
    (Module('foo'), []),
    (Module('foo', [FunctionDefinition(Name('bar'), [], SimpleStatement([ReturnStatement()]))]), [FunctionDefinition(Name('bar'), [], SimpleStatement([ReturnStatement()]))]),
])
# yapf: enable # pylint: enable=line-too-long
def test_iterate_children(module: Module, expected_children_list: NodeList) -> None:
    """Test arborista.nodes.python.module.iterate_children."""
    children: NodeIterator = module.iterate_children()
    children_list: NodeList = list(children)

    assert children_list == expected_children_list
