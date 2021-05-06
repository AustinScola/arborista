"""Test arborista.deparsers.python.compound_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.compound_statement_deparser import CompoundStatementDeparser
from arborista.nodes.python.class_definition import ClassDefinition
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.expression_list import ExpressionList
from arborista.nodes.python.for_statement import ForStatement
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.if_ import If
from arborista.nodes.python.if_statement import IfStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.compound_statement_deparser.CompoundStatementDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(CompoundStatementDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('compound_statement, indent, expected_string', [
    (FunctionDefinition(Name('foo'), parameters=Parameters(), body=SimpleStatement([ReturnStatement()])), '', 'def foo():return\n'),
    (FunctionDefinition(Name('foo'), parameters=Parameters(), body=SimpleStatement([ReturnStatement()])), '    ', '    def foo():return\n'),
    (FunctionDefinition(Name('foo'), parameters=Parameters(), body=SimpleStatement([ReturnStatement()])), '\t', '\tdef foo():return\n'),
    (ClassDefinition(Name('Foo'), None, SimpleStatement([PassStatement()])), '', 'class Foo:pass\n'),
    (ClassDefinition(Name('Foo'), None, SimpleStatement([PassStatement()])), '    ', '    class Foo:pass\n'),
    (IfStatement(If(Name('foo'), SimpleStatement([PassStatement()])), [], None), '', 'if foo:pass\n'),
    (IfStatement(If(Name('foo'), SimpleStatement([PassStatement()])), [], None), '    ', '    if foo:pass\n'),
    (ForStatement(ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), None), '', 'for foo in bar:pass\n'),
    (ForStatement(ExpressionList(Name('foo'), []), ExpressionList(Name('bar'), []), SimpleStatement([PassStatement()]), None), '    ', '    for foo in bar:pass\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_compound_statement(compound_statement: CompoundStatement, indent: str,
                                    expected_string: str) -> None:
    """Test arborista.deparsers.python.compound_statement_deparser.CompoundStatementDeparser.deparse_compound_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = CompoundStatementDeparser.deparse_compound_statement(compound_statement, indent)

    assert string == expected_string
