"""Test arborista.nodes.python.module."""
from typing import Optional

import pytest

from arborista.nodes.python.module import Module
from arborista.nodes.python.statement import StatementList, Statements


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
