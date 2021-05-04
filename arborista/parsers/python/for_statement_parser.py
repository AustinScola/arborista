"""Parser for a Python for statement."""
from typing import Optional

import libcst

from arborista.nodes.python.else_ import Else
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.expression_list import ExpressionList
from arborista.nodes.python.for_statement import ForStatement
from arborista.nodes.python.suite import Suite
from arborista.parser import Parser
from arborista.parsers.python.else_parser import ElseParser, LibcstElse
from arborista.parsers.python.expression_list_parser import (ExpressionListParser,
                                                             LibcstExpressionList)
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression
from arborista.parsers.python.suite_parser import LibcstSuite, SuiteParser

LibcstForStatement = libcst.For


class ForStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python for statement."""
    @staticmethod
    def parse_for_statement(libcst_for_statement: LibcstForStatement) -> ForStatement:
        """Parse a Python for statement."""
        values: ExpressionList
        if isinstance(libcst_for_statement.target,
                      libcst.Tuple) and not (libcst_for_statement.target.lpar
                                             or libcst_for_statement.target.rpar):
            libcst_tuple: libcst.Tuple = libcst_for_statement.target
            libcst_values: LibcstExpressionList = [
                libcst_element.value for libcst_element in libcst_tuple.elements
            ]
            values = ExpressionListParser.parse_expression_list(libcst_values)
        else:
            libcst_value: LibcstExpression = libcst_for_statement.target
            value: Expression = ExpressionParser.parse_expression(libcst_value)
            values = ExpressionList(value, [])

        sources: ExpressionList
        if isinstance(libcst_for_statement.iter,
                      libcst.Tuple) and not (libcst_for_statement.target.lpar
                                             or libcst_for_statement.target.rpar):
            libcst_tuple = libcst_for_statement.iter
            libcst_sources: LibcstExpressionList = [
                libcst_element.value for libcst_element in libcst_tuple.elements
            ]
            sources = ExpressionListParser.parse_expression_list(libcst_sources)
        else:
            libcst_source: LibcstExpression = libcst_for_statement.iter
            source: Expression = ExpressionParser.parse_expression(libcst_source)
            sources = ExpressionList(source, [])

        libcst_body: LibcstSuite = libcst_for_statement.body
        body: Suite = SuiteParser.parse_suite(libcst_body)

        else_: Optional[Else]
        libcst_else: Optional[LibcstElse] = libcst_for_statement.orelse
        if libcst_else is None:
            else_ = None
        else:
            else_ = ElseParser.parse_else(libcst_else)

        for_statement: ForStatement = ForStatement(values, sources, body, else_)

        return for_statement
