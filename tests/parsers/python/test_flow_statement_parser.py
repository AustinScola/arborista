"""Test arborista.parsers.python.flow_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.parser import Parser
from arborista.parsers.python.flow_statement_parser import FlowStatementParser, LibcstFlowStatement


def test_inheritance() -> None:
    """Test arborista.parsers.python.flow_statement_parser.FlowStatementParser inheritance."""
    assert issubclass(FlowStatementParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_flow_statement, expected_flow_statement', [
    (libcst.Return(), ReturnStatement()),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_flow_statement(libcst_flow_statement: LibcstFlowStatement,
                              expected_flow_statement: FlowStatement) -> None:
    """Test arborista.parsers.python.flow_statement_parser.FlowStatementParser.parse_flow_statement."""  # pylint: disable=line-too-long
    flow_statement: FlowStatement = FlowStatementParser.parse_flow_statement(libcst_flow_statement)
    assert flow_statement == expected_flow_statement
