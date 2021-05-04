"""Test arborista.deparsers.python.small_statement_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.small_statement_deparser import SmallStatementDeparser
from arborista.nodes.python.annotated_assignment_statement import AnnotatedAssignmentStatement
from arborista.nodes.python.assignment_statement import AssignmentStatement
from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.expression_statement import ExpressionStatement
from arborista.nodes.python.import_dotted_name import ImportDottedName
from arborista.nodes.python.name import Name
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.small_statement import SmallStatement
from arborista.nodes.python.string import String


def test_inheritance() -> None:
    """Test arborista.deparsers.python.small_statement_deparser.SmallStatementDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(SmallStatementDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('small_statement, expected_string', [
    (ExpressionStatement(String(None, SingleQuotedShortString('foo'))), "'foo'"),
    (ReturnStatement(), 'return'),
    (PassStatement(), 'pass'),
    (ImportDottedName(DottedNameAsNames(DottedNameAsName(DottedName(Name('foo'), []), None), [])), 'import foo'),
    (AssignmentStatement(AssignmentTargets(Name('foo'), []), Name('bar')), 'foo = bar'),
    (AnnotatedAssignmentStatement(Name('foo'), Name('Foo'), Name('bar')), 'foo: Foo = bar'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparser_small_statement(small_statement: SmallStatement, expected_string: str) -> None:
    """Test arborista.deparsers.python.small_statement_deparser.SmallStatementDeparser.deparse_small_statement."""  # pylint: disable=line-too-long, useless-suppression
    string: str = SmallStatementDeparser.deparse_small_statement(small_statement)

    assert string == expected_string
