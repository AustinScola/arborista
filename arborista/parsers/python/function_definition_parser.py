"""Parser for a Python function definition."""
import libcst

from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import ParameterList
from arborista.nodes.python.suite import Suite
from arborista.parser import Parser
from arborista.parsers.python.name_parser import LibcstName, NameParser
from arborista.parsers.python.parameter_parser import LibcstParameters, ParameterParser

LibcstFunctionDefinition = libcst.FunctionDef


class FunctionDefinitionParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python function definition."""
    @staticmethod
    def parse_function_definition(
            libcst_function_definition: LibcstFunctionDefinition) -> FunctionDefinition:
        """Parse a Python function definition."""
        from arborista.parsers.python.suite_parser import (LibcstSuite, SuiteParser)  # isort: skip # pylint: disable=import-outside-toplevel

        libcst_name: LibcstName = libcst_function_definition.name
        name: Name = NameParser.parse_name(libcst_name)

        libcst_parameters: LibcstParameters = libcst_function_definition.params
        parameters: ParameterList = ParameterParser.parse_parameters(libcst_parameters)

        libcst_body: LibcstSuite = libcst_function_definition.body
        body: Suite = SuiteParser.parse_suite(libcst_body)

        function_definition: FunctionDefinition = FunctionDefinition(name, parameters, body)
        return function_definition