"""Test arborista.nodes.python.simple_statement."""
import pytest

from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.small_statement import SmallStatements


# yapf: disable
@pytest.mark.parametrize('small_statements', [
    ([]),
])
# yapf: enable
def test_simple_statement_init(small_statements: SmallStatements) -> None:
    """Test arborista.nodes.python.simple_statement.__init__."""
    simple_statement: SimpleStatement = SimpleStatement(small_statements)

    assert simple_statement.small_statements == small_statements