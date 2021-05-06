"""Parser for a Python function call."""
import libcst

from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_call import FunctionCall
from arborista.parser import Parser

LibcstFunctionCall = libcst.Call


class FunctionCallParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python function call."""
    @staticmethod
    def parse_function_call(libcst_function_call: LibcstFunctionCall) -> FunctionCall:
        """Parse a Python function call."""
        from arborista.parsers.python.expression_parser import (  # pylint: disable=import-outside-toplevel
            ExpressionParser, LibcstExpression)

        libst_function: LibcstExpression = libcst_function_call.func
        function: Expression = ExpressionParser.parse_expression(libst_function)

        from arborista.parsers.python.arguments_parser import (  # pylint: disable=import-outside-toplevel
            ArgumentsParser, LibcstArguments)

        libcst_arguments: LibcstArguments = libcst_function_call.args
        arguments: Arguments = ArgumentsParser.parse_arguments(libcst_arguments)

        function_call: FunctionCall = FunctionCall(function, arguments)
        return function_call
