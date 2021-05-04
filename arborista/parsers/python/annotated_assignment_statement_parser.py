"""A parser for Python annotated assignment statements."""
from typing import Optional

import libcst

from arborista.nodes.python.annotated_assignment_statement import AnnotatedAssignmentStatement
from arborista.nodes.python.expression import Expression
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression

LibcstAnnotatedAssignmentStatement = libcst.AnnAssign


class AnnotatedAssignmentStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for Python annotated assignment statements."""
    @staticmethod
    def parse_annotated_assignment_statement(
        libcst_annotated_assignment_statement: LibcstAnnotatedAssignmentStatement
    ) -> AnnotatedAssignmentStatement:
        """Parser a Python annotated assignment statement."""
        libcst_target: LibcstExpression = libcst_annotated_assignment_statement.target
        target: Expression = ExpressionParser.parse_expression(libcst_target)

        libcst_annotation: LibcstExpression = \
            libcst_annotated_assignment_statement.annotation.annotation
        annotation: Expression = ExpressionParser.parse_expression(libcst_annotation)

        libcst_value: Optional[LibcstExpression] = libcst_annotated_assignment_statement.value
        value: Optional[Expression]
        if libcst_value is None:
            value = None
        else:
            value = ExpressionParser.parse_expression(libcst_value)

        annotated_assignment_statement: AnnotatedAssignmentStatement = \
            AnnotatedAssignmentStatement(target, annotation, value)

        return annotated_assignment_statement
