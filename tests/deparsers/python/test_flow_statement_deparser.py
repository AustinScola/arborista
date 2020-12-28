"""Test arborista.deparsers.python.flow_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.flow_statement_deparser import FlowStatementDeparser
from arborista.nodes.python.break_statement import BreakStatement
from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.return_statement import ReturnStatement


def test_inheritance() -> None:
    """Test arborista.deparsers.python.flow_statement_deparser.FlowStatementDeparser inheritance."""
    assert issubclass(FlowStatementDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('flow_statement, expected_string', [
    (BreakStatement(), 'break'),
    (ReturnStatement(), 'return'),
])
# yapf: enable
def test_deparse_flow_statement(flow_statement: FlowStatement, expected_string: str) -> None:
    """Test arborista.deparsers.python.flow_statement_deparser.FlowStatementDeparser.deparse_flow_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = FlowStatementDeparser.deparse_flow_statement(flow_statement)
    assert string == expected_string
