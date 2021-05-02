"""Deparser for a Python function call."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.arguments_deparser import ArgumentsDeparser
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_call import FunctionCall


class FunctionCallDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python function call."""
    @staticmethod
    def deparse_function_call(function_call: FunctionCall) -> str:
        """Deparse a Python function call."""
        string: str

        from arborista.deparsers.python.expression_deparser import \
            ExpressionDeparser  # pylint: disable=import-outside-toplevel

        function: Expression = function_call.function
        function_string: str = ExpressionDeparser.deparse_expression(function)

        arguments: Optional[Arguments] = function_call.arguments
        if arguments is None:
            string = function_string + '()'
        else:
            arguments_string: str = ArgumentsDeparser.deparse_arguments(arguments)
            string = function_string + '(' + arguments_string + ')'

        return string
