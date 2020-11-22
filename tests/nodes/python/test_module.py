"""Test arborista.nodes.python.module."""
from typing import Any, Optional

import pytest

from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.module import Module
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.statement import StatementList, Statements


def test_inheritance() -> None:
    """Test arborista.nodes.python.module.Module inheritance."""
    assert issubclass(Module, PythonNode)


# yapf: disable
@pytest.mark.parametrize('name, statements, pass_statements, expected_statements', [
    ('foo', [], True, []),
    ('foo', iter([]), True, []),
    ('foo', None, False, []),
])
# yapf: enable
def test_module_init(name: str, statements: Optional[Statements], pass_statements: bool,
                     expected_statements: StatementList) -> None:
    """Test arborista.nodes.python.module.__init__."""
    module: Module
    if pass_statements:
        module = Module(name, statements)
    else:
        module = Module(name)

    assert module.name == name
    assert module.statements == expected_statements


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('module, other, expected_equality', [
    (Module('foo'), 'bar', False),
    (Module('foo'), Module('bar'), False),
    (Module('foo', [FunctionDefinition(Name('bar'), [], [])]), Module('foo'), False),
    (Module('foo'), Module('foo'), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(module: Module, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.module.__eq__."""
    equality: bool = module == other
    assert equality == expected_equality
