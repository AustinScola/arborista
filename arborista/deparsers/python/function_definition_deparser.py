"""Deparser for a Python function definition."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.decorator_deparser import DecoratorDeparser
from arborista.deparsers.python.expression_deparser import ExpressionDeparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.deparsers.python.parameters_deparser import ParametersDeparser
from arborista.deparsers.python.suite_deparser import SuiteDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.decorator import Decorators
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_definition import FunctionDefinition


class FunctionDefinitionDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python function definition."""
    @staticmethod
    def deparse_function_definition(function_definition: FunctionDefinition, indent: str) -> str:
        """Deparse a Python function definition."""
        string: str = ''

        decorators: Decorators = function_definition.decorators
        if decorators:
            decorators_string = DecoratorDeparser.deparse_decorators(decorators, indent)
            string += decorators_string

        string += indent + 'def '

        name_string: str = NameDeparser.deparse_name(function_definition.name)
        string += name_string

        string += '('

        parameters_string: str = ParametersDeparser.deparse_parameters(
            function_definition.parameters)
        string += parameters_string

        string += ')'

        returns: Optional[Expression] = function_definition.returns
        if returns is not None:
            returns_string = ExpressionDeparser.deparse_expression(returns)
            string += ' -> ' + returns_string

        string += ':'

        body_string: str
        if isinstance(function_definition.body, Block):
            string += '\n'
            body_string = SuiteDeparser.deparse_suite(function_definition.body, indent)
        else:
            body_string = SuiteDeparser.deparse_suite(function_definition.body, '')

        string += body_string
        return string
