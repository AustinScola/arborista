"""Test arborista.deparsers.python.suite_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.suite_deparser import SuiteDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite


def test_inheritance() -> None:
    """Test arborista.deparsers.python.suite_deparser.SuiteDeparser inheritance."""
    assert issubclass(SuiteDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('suite, indent, expected_string', [
    (SimpleStatement([ReturnStatement()]), '', 'return\n'),
    (SimpleStatement([ReturnStatement()]), '    ', '    return\n'),
    (SimpleStatement([ReturnStatement()]), '\t', '\treturn\n'),
    (Block([SimpleStatement([ReturnStatement()])], '    '), '', '    return\n'),
    (Block([SimpleStatement([ReturnStatement()])], '    '), '    ', '        return\n'),
    (Block([SimpleStatement([ReturnStatement()])], '    '), '\t', '\t    return\n'),
])
# yapf: enable
def test_deparse_suite(suite: Suite, indent: str, expected_string: str) -> None:
    """Test arborista.deparsers.python.suite_deparser.SuiteDeparser.deparse_suite."""
    string: str = SuiteDeparser.deparse_suite(suite, indent)

    assert string == expected_string
