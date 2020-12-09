"""Test arborista.deparsers.python.statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.statement_deparser import StatementDeparser
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.statement import Statement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.statement_deparser.StatementDeparser inheritance."""
    assert issubclass(StatementDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('statement, indent, expected_string', [
    (FunctionDefinition(Name('foo'), parameters=[], body=SimpleStatement([ReturnStatement()])), '', 'def foo():return\n'),
    (SimpleStatement([ReturnStatement()]), '', 'return\n'),

])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_statement(statement: Statement, indent: str, expected_string: str) -> None:
    """Test arborista.deparsers.python.statement_deparser.StatementDeparser.deparse_statement."""
    string: str = StatementDeparser.deparse_statement(statement, indent)
    assert string == expected_string
