"""Parser for a Python function definition."""
from typing import Optional

import libcst

from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.suite import Suite
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser
from arborista.parsers.python.name_parser import LibcstName, NameParser
from arborista.parsers.python.parameters_parser import LibcstParameters, ParametersParser

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
        parameters: Parameters = ParametersParser.parse_parameters(libcst_parameters)

        libcst_body: LibcstSuite = libcst_function_definition.body
        body: Suite = SuiteParser.parse_suite(libcst_body)

        returns: Optional[Expression]
        if libcst_function_definition.returns is None:
            returns = None
        else:
            libcst_returns = libcst_function_definition.returns.annotation
            returns = ExpressionParser.parse_expression(libcst_returns)

        function_definition: FunctionDefinition = FunctionDefinition(name,
                                                                     parameters,
                                                                     body,
                                                                     returns=returns)
        function_definition.set_parent_in_children()

        return function_definition
