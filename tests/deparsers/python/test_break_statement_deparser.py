"""Test arborista.deparsers.python.break_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.break_statement_deparser import BreakStatementDeparser
from arborista.nodes.python.break_statement import BreakStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.break_statement_deparser.BreakStatementDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(BreakStatementDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('break_statement, expected_string', [
    (BreakStatement(), 'break'),
])
# yapf: enable
def test_deparse_break_statement(break_statement: BreakStatement, expected_string: str) -> None:
    """Test arborista.deparsers.python.break_statement_deparser.BreakStatementDeparser.deparse_break_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = BreakStatementDeparser.deparse_break_statement(break_statement)

    assert string == expected_string
