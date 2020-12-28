"""Test arborista.deparsers.python.continue_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.continue_statement_deparser import ContinueStatementDeparser
from arborista.nodes.python.continue_statement import ContinueStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.continue_statement_deparser.ContinueStatementDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ContinueStatementDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('continue_statement, expected_string', [
    (ContinueStatement(), 'continue'),
])
# yapf: enable
def test_deparse_continue_statement(continue_statement: ContinueStatement,
                                    expected_string: str) -> None:
    """Test arborista.deparsers.python.continue_statement_deparser.ContinueStatementDeparser.deparse_continue_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = ContinueStatementDeparser.deparse_continue_statement(continue_statement)
    assert string == expected_string
