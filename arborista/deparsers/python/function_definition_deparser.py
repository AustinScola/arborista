"""Deparser for a Python function definition."""
from typing import Iterator

from arborista.deparser import Deparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.deparsers.python.parameter_deparser import ParameterDeparser
from arborista.deparsers.python.suite_deparser import SuiteDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.function_definition import FunctionDefinition


class FunctionDefinitionDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python function definition."""
    @staticmethod
    def deparse_function_definition(function_definition: FunctionDefinition, indent: str) -> str:
        """Deparse a Python function definition."""
        string: str = indent
        string += 'def '

        name_string: str = NameDeparser.deparse_name(function_definition.name)
        string += name_string

        string += '('

        parameter_strings: Iterator[str] = (ParameterDeparser.deparse_parameter(parameter)
                                            for parameter in function_definition.parameters)
        parameters_string: str = ','.join(parameter_strings)
        string += parameters_string

        string += '):'
        body_string: str
        if isinstance(function_definition.body, Block):
            string += '\n'
            body_string = SuiteDeparser.deparse_suite(function_definition.body, indent)
        else:
            body_string = SuiteDeparser.deparse_suite(function_definition.body, '')

        string += body_string
        return string
