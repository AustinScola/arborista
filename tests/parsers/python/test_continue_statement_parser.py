"""Test arborista.parsers.python.continue_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.continue_statement import ContinueStatement
from arborista.parser import Parser
from arborista.parsers.python.continue_statement_parser import (ContinueStatementParser,
                                                                LibcstContinueStatement)


def test_inheritance() -> None:
    """Test arborista.parsers.python.continue_statement_parser.ContinueStatementParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(ContinueStatementParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_continue_statement, expected_continue_statement', [
    (libcst.Continue(), ContinueStatement()),
])
# yapf: enable
def test_parse_continue_statement(libcst_continue_statement: LibcstContinueStatement,
                                  expected_continue_statement: ContinueStatement) -> None:
    """Test arborista.parsers.python.continue_statement_parser.ContinueStatementParser.parse_continue_statement."""  # pylint: disable=line-too-long, useless-suppression
    continue_statement: ContinueStatement = ContinueStatementParser.parse_continue_statement(
        libcst_continue_statement)

    assert continue_statement == expected_continue_statement
