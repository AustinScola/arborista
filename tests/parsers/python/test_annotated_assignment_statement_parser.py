"""Test arborista.parsers.python.annotated_assignment_statement_parser."""
import libcst
import pytest

from arborista.nodes.python.annotated_assignment_statement import AnnotatedAssignmentStatement
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.annotated_assignment_statement_parser import (
    AnnotatedAssignmentStatementParser, LibcstAnnotatedAssignmentStatement)


def test_libcst_annotated_assignment_statement() -> None:
    """Test arborista.parsers.python.annotated_assignment_statement_parser.LibcstAnnotatedAssignmentStatement"""  # pylint: disable=line-too-long, useless-suppression
    assert LibcstAnnotatedAssignmentStatement == libcst.AnnAssign


def test_inheritance() -> None:
    """Test arborista.parsers.python.annotated_assignment_statement_parser.AnnotatedAssignmentStatementParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(AnnotatedAssignmentStatementParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_annotated_assignment_statement, expected_annotated_assignment_statement', [
    (libcst.AnnAssign(libcst.Name('foo'), libcst.Annotation(libcst.Name('Foo')), None), AnnotatedAssignmentStatement(Name('foo'), Name('Foo'), None)),
    (libcst.AnnAssign(libcst.Name('foo'), libcst.Annotation(libcst.Name('Foo')), libcst.Name('bar')), AnnotatedAssignmentStatement(Name('foo'), Name('Foo'), Name('bar'))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_annotated_assignment_statement(
        libcst_annotated_assignment_statement: LibcstAnnotatedAssignmentStatement,
        expected_annotated_assignment_statement: AnnotatedAssignmentStatement) -> None:
    """Test arborista.parsers.python.annotated_assignment_statement_parser.AnnotatedAssignmentStatementParser.parse_annotated_assignment_statement."""  # pylint: disable=line-too-long, useless-suppression
    annotated_assignment_statement: AnnotatedAssignmentStatement = AnnotatedAssignmentStatementParser.parse_annotated_assignment_statement(
        libcst_annotated_assignment_statement)

    assert annotated_assignment_statement == expected_annotated_assignment_statement
