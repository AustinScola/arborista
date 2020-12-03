"""Test arborista.parsers.python.suite_parser."""
import libcst
import pytest

from arborista.nodes.python.block import Block
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite
from arborista.parser import Parser
from arborista.parsers.python.suite_parser import LibcstSuite, SuiteParser


def test_inheritance() -> None:
    """Test arborista.parsers.python.suite_parser.SuiteParser inheritance."""
    assert issubclass(SuiteParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_suite, expected_suite', [
    (libcst.SimpleStatementSuite([]), SimpleStatement([])),
    (libcst.IndentedBlock([libcst.SimpleStatementLine([libcst.Return()])]), Block([SimpleStatement(small_statements=[ReturnStatement()])])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_suite(libcst_suite: LibcstSuite, expected_suite: Suite) -> None:
    """Test arborista.parsers.python.suite_parser.SuiteParser.parse_suite."""
    suite: Suite = SuiteParser.parse_suite(libcst_suite)
    assert suite == expected_suite
