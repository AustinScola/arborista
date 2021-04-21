"""Parser for a Python function call."""
from typing import Optional

import libcst

from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_call import FunctionCall
from arborista.parser import Parser
from arborista.parsers.python.arguments_parser import ArgumentsParser, LibcstArguments
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression

LibcstFunctionCall = libcst.Call


class FunctionCallParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python function call."""
    @staticmethod
    def parse_function_call(libcst_function_call: LibcstFunctionCall) -> FunctionCall:
        """Parse a Python function call."""
        libst_function: LibcstExpression = libcst_function_call.func
        function: Expression = ExpressionParser.parse_expression(libst_function)

        arguments: Optional[Arguments]
        libcst_arguments: LibcstArguments = libcst_function_call.args
        if not libcst_arguments:
            arguments = None
        else:
            arguments = ArgumentsParser.parse_arguments(libcst_arguments)

        function_call: FunctionCall = FunctionCall(function, arguments)
        return function_call
