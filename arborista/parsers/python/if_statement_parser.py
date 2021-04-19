"""A parser for a Python if statement."""
from typing import List, Optional, Union

import libcst

from arborista.nodes.python.elif_ import Elif
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.if_ import If
from arborista.nodes.python.if_statement import IfStatement
from arborista.nodes.python.suite import Suite
from arborista.parser import Parser
from arborista.parsers.python.else_parser import ElseParser, LibcstElse
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression
from arborista.parsers.python.suite_parser import LibcstSuite, SuiteParser

LibcstIfStatement = libcst.If


class IfStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python if statement."""
    @staticmethod
    def parse_if_statement(libcst_if_statement: LibcstIfStatement) -> IfStatement:  # pylint: disable=too-many-locals
        """Parse a Python if statement."""
        libcst_if_condition: LibcstExpression = libcst_if_statement.test
        if_condition: Expression = ExpressionParser.parse_expression(libcst_if_condition)

        libcst_if_body: LibcstSuite = libcst_if_statement.body
        if_body: Suite = SuiteParser.parse_suite(libcst_if_body)

        if_: If = If(if_condition, if_body)

        elifs: List[Elif] = []
        else_: Optional[Else]
        libcst_elif_or_else: Union[libcst.If, LibcstElse, None] = libcst_if_statement.orelse
        while True:
            if isinstance(libcst_elif_or_else, libcst.If):
                libcst_elif = libcst_elif_or_else

                libcst_elif_condition: LibcstExpression = libcst_elif.test
                elif_condition: Expression = ExpressionParser.parse_expression(
                    libcst_elif_condition)

                libcst_elif_body: LibcstSuite = libcst_elif.body
                elif_body: Suite = SuiteParser.parse_suite(libcst_elif_body)

                elif_: Elif = Elif(elif_condition, elif_body)
                elifs.append(elif_)

                libcst_elif_or_else = libcst_if_statement.orelse

            if isinstance(libcst_elif_or_else, LibcstElse):
                libcst_else: LibcstElse = libcst_elif_or_else
                else_ = ElseParser.parse_else(libcst_else)
                break

            else_ = None
            break

        if_statement: IfStatement = IfStatement(if_, elifs, else_)

        return if_statement
