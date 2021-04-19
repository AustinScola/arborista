"""Test arborista.parsers.python.if_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.elif_ import Elif
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.if_ import If
from arborista.nodes.python.if_statement import IfStatement
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.parser import Parser
from arborista.parsers.python.if_statement_parser import IfStatementParser, LibcstIfStatement


def test_libcst_if_statement() -> None:
    """Test arborista.parsers.python.if_statement_parser.LibcstIfStatement."""
    assert LibcstIfStatement == libcst.If


def test_inheritance() -> None:
    """Test arborista.parsers.python.if_statement_parser.IfStatementParser inheritance."""
    assert issubclass(IfStatementParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_if_statement, expected_if_statement', [
    (libcst.If(libcst.Integer('1'), libcst.SimpleStatementSuite([libcst.Pass()])), IfStatement(If(Integer(1), SimpleStatement([PassStatement()])), [], None)),
    (libcst.If(libcst.Integer('1'), libcst.SimpleStatementSuite([libcst.Pass()]), libcst.Else(libcst.SimpleStatementSuite([libcst.Pass()]))), IfStatement(If(Integer(1), SimpleStatement([PassStatement()])), [], Else(SimpleStatement([PassStatement()])))),
    (libcst.If(libcst.Integer('1'), libcst.SimpleStatementSuite([libcst.Pass()]), libcst.If(libcst.Integer('2'), libcst.SimpleStatementSuite([libcst.Pass()]))), IfStatement(If(Integer(1), SimpleStatement([PassStatement()])), [Elif(Integer(2), SimpleStatement([PassStatement()]))], None)),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_if_statement(libcst_if_statement: LibcstIfStatement,
                            expected_if_statement: IfStatement) -> None:
    """Test arborista.parsers.python.if_statement_parser.IfStatementParser.parse_if_statement."""
    if_statement: IfStatement = IfStatementParser.parse_if_statement(libcst_if_statement)

    assert if_statement == expected_if_statement
