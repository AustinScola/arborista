"""Test arborista.nodes.python.module."""
import pytest

from arborista.nodes.python.module import Module
from arborista.nodes.python.statement import Statements


# yapf: disable
@pytest.mark.parametrize('name, statements', [
    ('foo', [])
])
# yapf: enable
def test_module_init(name: str, statements: Statements) -> None:
    """Test arborista.nodes.python.module.__init__."""
    module: Module = Module(name, statements)

    assert module.name == name
    assert module.statements == statements
