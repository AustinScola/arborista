"""Test arborista.parsers.python.simple_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.parser import Parser
from arborista.parsers.python.simple_statement_parser import (LibcstSimpleStatement,
                                                              SimpleStatementParser)
from testing_helpers.assert_parent_set_in_children import assert_parent_set_in_children


def test_inheritance() -> None:
    """Test arborista.parsers.python.simple_statement_parser.SimpleStatementParser inheritance."""
    assert issubclass(SimpleStatementParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_simple_statement, expected_simple_statement', [
    (libcst.SimpleStatementLine([libcst.Return()]), SimpleStatement([ReturnStatement()])),
])
# yapf: enable
def test_parse_simple_statement(libcst_simple_statement: LibcstSimpleStatement,
                                expected_simple_statement: SimpleStatement) -> None:
    """Test arborista.parsers.python.simple_statement_parser.SimpleStatementParser.parse_simple_statement."""  # pylint: disable=line-too-long, useless-suppression
    simple_statement: SimpleStatement = SimpleStatementParser.parse_simple_statement(
        libcst_simple_statement)

    assert simple_statement == expected_simple_statement
    assert_parent_set_in_children(simple_statement)
