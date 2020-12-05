"""Test arborista.parsers.python.return_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.return_statement import ReturnStatement
from arborista.parser import Parser
from arborista.parsers.python.return_statement_parser import (LibcstReturnStatement,
                                                              ReturnStatementParser)


def test_inheritance() -> None:
    """Test arborista.parsers.python.return_statement_parser.ReturnStatementParser inheritance."""
    assert issubclass(ReturnStatementParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_return_statement, expected_return_statement', [
    (libcst.Return(), ReturnStatement()),
])
# yapf: enable
def test_parse_return_statement(libcst_return_statement: LibcstReturnStatement,
                                expected_return_statement: ReturnStatement) -> None:
    """Test arborista.parsers.python.return_statement_parser.ReturnStatementParser.parse_return_statement."""  # pylint: disable=line-too-long, useless-suppression
    return_statement: ReturnStatement = ReturnStatementParser.parse_return_statement(
        libcst_return_statement)
    assert return_statement == expected_return_statement
