"""Test arborista.parsers.python.compound_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.block import Block
from arborista.nodes.python.class_definition import ClassDefinition
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.expression_list import ExpressionList
from arborista.nodes.python.for_statement import ForStatement
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.if_ import If
from arborista.nodes.python.if_statement import IfStatement
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.parser import Parser
from arborista.parsers.python.compound_statement_parser import (CompoundStatementParser,
                                                                LibcstCompoundStatement)


def test_inheritance() -> None:
    """Test arborista.parsers.python.compound_statement_parser.CompoundStatementParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(CompoundStatementParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_compound_statement, expected_compound_statement', [
    (libcst.If(libcst.Integer('1'), libcst.SimpleStatementSuite([libcst.Pass()])), IfStatement(If(Integer(1), SimpleStatement([PassStatement()])), [], None)),
    (libcst.FunctionDef(name=libcst.Name(value='foo'), params=libcst.Parameters(), body=libcst.IndentedBlock([libcst.SimpleStatementLine([libcst.Return()])])), FunctionDefinition(name=Name('foo'), parameters=Parameters(), body=Block([SimpleStatement([ReturnStatement()])], '    '))),
    (libcst.ClassDef(libcst.Name('Foo'), libcst.SimpleStatementSuite([libcst.Pass()])), ClassDefinition(Name('Foo'), None, SimpleStatement([PassStatement()]))),
    (libcst.For(libcst.Name('foo'), libcst.Name('bar'), libcst.SimpleStatementSuite([libcst.Pass()])), ForStatement(ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), None)),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_compound_statement(libcst_compound_statement: LibcstCompoundStatement,
                                  expected_compound_statement: CompoundStatement) -> None:
    """Test arborista.parsers.python.compound_statement_parser.CompoundStatementParser.parse_compound_statement."""  # pylint: disable=line-too-long, useless-suppression
    compound_statement: CompoundStatement = CompoundStatementParser.parse_compound_statement(
        libcst_compound_statement)

    assert compound_statement == expected_compound_statement
