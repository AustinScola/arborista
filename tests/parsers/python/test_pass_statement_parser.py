"""Test arborista.parsers.python.pass_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.pass_statement import PassStatement
from arborista.parser import Parser
from arborista.parsers.python.pass_statement_parser import LibcstPassStatement, PassStatementParser


def test_inheritance() -> None:
    """Test arborista.parsers.python.pass_statement_parser.PassStatementParser inheritance."""
    assert issubclass(PassStatementParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_pass_statement, expected_pass_statement', [
    (libcst.Pass(), PassStatement()),
])
# yapf: enable
def test_parse_pass_statement(libcst_pass_statement: LibcstPassStatement,
                              expected_pass_statement: PassStatement) -> None:
    """Test arborista.parsers.python.pass_statement_parser.PassStatementParser.parse_pass_statement."""  # pylint: disable=line-too-long, useless-suppression
    pass_statement: PassStatement = PassStatementParser.parse_pass_statement(libcst_pass_statement)

    assert pass_statement == expected_pass_statement
