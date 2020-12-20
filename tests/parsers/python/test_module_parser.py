"""Test arborista.parsing.python.module_parser."""
from pathlib import Path

import pytest

from arborista.nodes.file_system.file import File
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

])
# yapf: enable # pylint: enable=line-too-long
def test_parse_module(string: str, name: str, expected_module: Module) -> None:
    """Test arborista.parsing.python.module_parser.ModuleParser.parse_module."""
    module = ModuleParser.parse_module(name, string)

    assert module == expected_module
    assert_parent_set_in_children(module)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('file_, expected_module', [
    (File(Path('foo.py'), ''), Module('foo')),
    (File(Path('foo.py'), 'def f(): return'), Module('foo', [FunctionDefinition(name=Name('f'), parameters=[], body=SimpleStatement([ReturnStatement()]))])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_module_from_file(file_: File, expected_module: Module) -> None:
    """Test arborista.parsing.python.module_parser.ModuleParser.parse_module_from_file."""
    module: Module = ModuleParser.parse_module_from_file(file_)

    assert module == expected_module
    assert_parent_set_in_children(module)
