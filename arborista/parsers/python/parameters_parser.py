"""A parser for Python parameters."""
from typing import List, Sequence

import libcst

from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.positional_parameter import PositionalParameter
from arborista.parser import Parser
from arborista.parsers.python.positional_parameter_parser import (LibcstPositionalParameter,
                                                                  PositionalParameterParser)

LibcstParameters = libcst.Parameters


class ParametersParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for Python parameters."""
    @staticmethod
    def parse_parameters(libcst_parameters: LibcstParameters) -> Parameters:
        """A parser for Python parameters."""
        positional_parameters: List[PositionalParameter] = []
        libcst_positionals: Sequence[LibcstPositionalParameter] = libcst_parameters.params
        for libcst_positional in libcst_positionals:
            positional_parameter: PositionalParameter = \
                PositionalParameterParser.parse_positional_parameter(libcst_positional)
            positional_parameters.append(positional_parameter)

        parameters: Parameters = Parameters(positional_parameters)

        return parameters
