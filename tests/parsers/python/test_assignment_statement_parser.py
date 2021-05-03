"""Test arborista.parsers.python.assignment_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.assignment_statement import AssignmentStatement
from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.assignment_statement_parser import (AssignmentStatementParser,
                                                                  LibcstAssignmentStatement)


def test_libcst_assignment_statement() -> None:
    """Test arborista.parsers.python.assignment_statement_parser.LibcstAssignmentStatement."""
    assert LibcstAssignmentStatement == libcst.Assign


def test_inheritance() -> None:
    """Test arborista.parsers.python.assignment_statement_parser.AssignmentStatementParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(AssignmentStatementParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_assignment_statement, expected_assignment_statement', [
    (libcst.Assign([libcst.AssignTarget(libcst.Name('foo'))], libcst.Name('bar')), AssignmentStatement(AssignmentTargets(Name('foo'), []), Name('bar'))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_assignment_statement(libcst_assignment_statement: LibcstAssignmentStatement,
                                    expected_assignment_statement: AssignmentStatement) -> None:
    """Test arborista.parsers.python.assignment_statement_parser.AssignmentStatementParser.parse_assignment_statement."""  # pylint: disable=line-too-long, useless-suppression
    assignment_statement: AssignmentStatement = AssignmentStatementParser.parse_assignment_statement(
        libcst_assignment_statement)

    assert assignment_statement == expected_assignment_statement
