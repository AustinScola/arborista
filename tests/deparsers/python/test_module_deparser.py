"""Test arborista.deparsers.python.module_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.module_deparser import ModuleDeparser
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.module import Module
from arborista.nodes.python.name import Name
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.module_deparser.ModuleDeparser inheritance."""
    assert issubclass(ModuleDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('module, expected_string', [
    (Module('foo', []), ''),
    (Module('foo', [SimpleStatement([ReturnStatement()])]), 'return\n'),
    (Module('foo', [SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()])]), 'return\nreturn\n'),
    (Module('foo', [SimpleStatement([ReturnStatement(), ReturnStatement()])]), 'return; return\n'),
    (Module('foo', [FunctionDefinition(Name('bar'), [], body=SimpleStatement([ReturnStatement()]))]), 'def bar():return\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_module(module: Module, expected_string: str) -> None:
    """Test arborista.deparsers.python.module_deparser.ModuleDeparser.deparse_module."""
    string: str = ModuleDeparser.deparse_module(module)

    assert string == expected_string
