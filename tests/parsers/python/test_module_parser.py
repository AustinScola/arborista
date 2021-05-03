"""Test arborista.parsing.python.module_parser."""
import pytest

from arborista.nodes.python.empty_line import EmptyLine
from arborista.nodes.python.expression_statement import ExpressionStatement
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.module import Module
from arborista.nodes.python.name import Name
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.parser import Parser
from arborista.parsers.python.module_parser import ModuleParser
from testing_helpers.assert_parent_set_in_children import assert_parent_set_in_children


def test_inheritance() -> None:
    """Test arborista.parsing.python.module_parser.ModuleParser inheritance."""
    assert issubclass(ModuleParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('string, name, expected_module', [
    ('', 'foo', Module('foo')),
    ('def foo(): return', 'foo', Module('foo', [FunctionDefinition(name=Name('foo'), parameters=[], body=SimpleStatement([ReturnStatement()]))])),
    ('a\n\nb', 'foo', Module('foo', [SimpleStatement([ExpressionStatement(Name('a'))]), EmptyLine(), SimpleStatement([ExpressionStatement(Name('b'))])])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_module(string: str, name: str, expected_module: Module) -> None:
    """Test arborista.parsing.python.module_parser.ModuleParser.parse_module."""
    module = ModuleParser.parse_module(name, string)

    assert module == expected_module
    assert_parent_set_in_children(module)
