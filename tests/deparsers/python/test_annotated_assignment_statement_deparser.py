"""Test arborista.deparsers.python.annotated_assignment_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.annotated_assignment_statement_deparser import \
    AnnotatedAssignmentStatementDeparser
from arborista.nodes.python.annotated_assignment_statement import AnnotatedAssignmentStatement
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.annotated_assignment_statement_deparser.AnnotatedAssignmentStatementDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(AnnotatedAssignmentStatementDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('annotated_assignment_statement, expected_string', [
    (AnnotatedAssignmentStatement(Name('foo'), Name('Foo'), None), 'foo: Foo'),
    (AnnotatedAssignmentStatement(Name('foo'), Name('Foo'), Name('bar')), 'foo: Foo = bar'),
])
# yapf: enable
def test_deparse_annotated_assignment_statement(
        annotated_assignment_statement: AnnotatedAssignmentStatement, expected_string: str) -> None:
    """Test arborista.deparsers.python.annotated_assignment_statement_deparser.AnnotatedAssignmentStatementDeparser.deparse_annotated_assignment_statement"""  # pylint: disable=line-too-long, useless-suppression
    string: str = AnnotatedAssignmentStatementDeparser.deparse_annotated_assignment_statement(
        annotated_assignment_statement)

    assert string == expected_string
