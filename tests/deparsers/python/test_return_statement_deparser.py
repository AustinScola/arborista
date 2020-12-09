"""Test arborista.deparsers.python.return_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.return_statement_deparser import ReturnStatementDeparser
from arborista.nodes.python.return_statement import ReturnStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.return_statement_deparser.ReturnStatementDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ReturnStatementDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('return_statement, expected_string', [
    (ReturnStatement(), 'return'),
])
# yapf: enable
def test_deparse_return_statement(return_statement: ReturnStatement, expected_string: str) -> None:
    """Test arborista.deparsers.python.return_statement_deparser.ReturnStatementDeparser.deparse_return_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = ReturnStatementDeparser.deparse_return_statement(return_statement)
    assert string == expected_string
