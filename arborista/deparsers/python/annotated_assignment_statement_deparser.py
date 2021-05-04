"""A deparser for Python annotated assignment statements."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.expression_deparser import ExpressionDeparser
from arborista.nodes.python.annotated_assignment_statement import AnnotatedAssignmentStatement
from arborista.nodes.python.expression import Expression


class AnnotatedAssignmentStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python annotated assignment statements."""
    @staticmethod
    def deparse_annotated_assignment_statement(
            annotated_assignment_statement: AnnotatedAssignmentStatement) -> str:
        """Deparser a Python annotated assignment statement."""
        string: str

        target: Expression = annotated_assignment_statement.target
        target_string: str = ExpressionDeparser.deparse_expression(target)

        annotation: Expression = annotated_assignment_statement.annotation
        annotation_string: str = ExpressionDeparser.deparse_expression(annotation)

        value: Optional[Expression] = annotated_assignment_statement.value
        if value is None:
            string = target_string + ': ' + annotation_string
        else:
            value_string: str = ExpressionDeparser.deparse_expression(value)
            string = target_string + ': ' + annotation_string + ' = ' + value_string

        return string
