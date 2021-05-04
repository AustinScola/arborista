"""Deparser for a Python for statement."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.else_deparser import ElseDeparser
from arborista.deparsers.python.expression_list_deparser import ExpressionListDeparser
from arborista.deparsers.python.suite_deparser import SuiteDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.expression_list import ExpressionList
from arborista.nodes.python.for_statement import ForStatement
from arborista.nodes.python.suite import Suite


class ForStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python for statement."""
    @staticmethod
    def deparse_for_statement(for_statement: ForStatement, indent: str) -> str:
        """Deparse a Python for statement."""
        string: str

        values: ExpressionList = for_statement.values
        values_string = ExpressionListDeparser.deparse_expression_list(values)

        sources: ExpressionList = for_statement.sources
        sources_string = ExpressionListDeparser.deparse_expression_list(sources)

        body: Suite = for_statement.body
        body_string: str
        if isinstance(body, Block):
            body_string = '\n' + SuiteDeparser.deparse_suite(body, indent)
        else:
            body_string = SuiteDeparser.deparse_suite(body, '')

        string = indent + "for " + values_string + " in " + sources_string + ":" + body_string

        else_: Optional[Else] = for_statement.else_
        if else_ is not None:
            else_string: str = ElseDeparser.deparse_else(else_, indent)
            string += else_string

        return string
