"""Test arborista.deparsers.python.assignment_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.assignment_statement_deparser import AssignmentStatementDeparser
from arborista.nodes.python.assignment_statement import AssignmentStatement
from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.assignment_statement_deparser.AssignmentStatementDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(AssignmentStatementDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('assignment_statement, expected_string', [
    (AssignmentStatement(AssignmentTargets(Name('foo'), []), Name('bar')), 'foo = bar'),
])
# yapf: enable
def test_deparse_assignment_statement(assignment_statement: AssignmentStatement,
                                      expected_string: str) -> None:
    """Test arborista.deparsers.python.assignment_statement_deparser.AssignmentStatementDeparser.deparse_assignment_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = AssignmentStatementDeparser.deparse_assignment_statement(assignment_statement)

    assert string == expected_string
