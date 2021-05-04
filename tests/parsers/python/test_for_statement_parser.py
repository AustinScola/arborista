"""Test arborista.parsers.python.for_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.else_ import Else
from arborista.nodes.python.expression_list import ExpressionList
from arborista.nodes.python.for_statement import ForStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.parser import Parser
from arborista.parsers.python.for_statement_parser import ForStatementParser, LibcstForStatement


def test_libcst_for_statement() -> None:
    """Test arborista.parsers.python.for_statement_parser.LibcstForStatement"""
    assert LibcstForStatement == libcst.For


def test_inheritance() -> None:
    """Test arborista.parsers.python.for_statement_parser.ForStatementParser inheritance."""
    assert issubclass(ForStatementParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_for_statement, expected_for_statement', [
    (libcst.For(libcst.Name('foo'), libcst.Name('bar'), libcst.SimpleStatementSuite([libcst.Pass()])), ForStatement(ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), None)),
    (libcst.For(libcst.Tuple([libcst.Element(libcst.Name('foo')), libcst.Element(libcst.Name('bar'))], lpar=[], rpar=[]), libcst.Name('baz'), libcst.SimpleStatementSuite([libcst.Pass()])), ForStatement(ExpressionList(Name('foo'), [Name('bar')]), ExpressionList(Name('baz'), []), SimpleStatement([PassStatement()]), None)),
    (libcst.For(libcst.Name('foo'), libcst.Tuple([libcst.Element(libcst.Name('bar')), libcst.Element(libcst.Name('baz'))], lpar=[], rpar=[]), libcst.SimpleStatementSuite([libcst.Pass()])), ForStatement(ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), [Name('baz')]), SimpleStatement([PassStatement()]), None)),
    (libcst.For(libcst.Name('foo'), libcst.Name('bar'), libcst.SimpleStatementSuite([libcst.Pass()]), libcst.Else(libcst.SimpleStatementSuite([libcst.Pass()]))), ForStatement(ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), Else(SimpleStatement([PassStatement()])))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_for_statement(libcst_for_statement: LibcstForStatement,
                             expected_for_statement: ForStatement) -> None:
    """Test arborista.parsers.python.for_statement_parser.ForStatementParser.parse_for_statement."""
    for_statement: ForStatement = ForStatementParser.parse_for_statement(libcst_for_statement)

    assert for_statement == expected_for_statement
