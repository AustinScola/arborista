"""Test arborista.parsers.python.break_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.break_statement import BreakStatement
from arborista.parser import Parser
from arborista.parsers.python.break_statement_parser import (BreakStatementParser,
                                                             LibcstBreakStatement)


def test_inheritance() -> None:
    """Test arborista.parsers.python.break_statement_parser.BreakStatementParser inheritance."""
    assert issubclass(BreakStatementParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_break_statement, expected_break_statement', [
    (libcst.Break(), BreakStatement()),
])
# yapf: enable
def test_parse_break_statement(libcst_break_statement: LibcstBreakStatement,
                               expected_break_statement: BreakStatement) -> None:
    """Test arborista.parsers.python.break_statement_parser.BreakStatementParser.parse_break_statement."""  # pylint: disable=line-too-long, useless-suppression
    break_statement: BreakStatement = BreakStatementParser.parse_break_statement(
        libcst_break_statement)
    assert break_statement == expected_break_statement
