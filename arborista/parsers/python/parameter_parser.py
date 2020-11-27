"""Parser for a Python parameter."""
import libcst

from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import Parameter, ParameterList
from arborista.parser import Parser
from arborista.parsers.python.name_parser import LibcstName, NameParser

LibcstParameter = libcst.Param
LibcstParameters = libcst.Parameters


class ParameterParser(Parser):
    """Parser for a Python parameter."""
    @staticmethod
    def parse_parameter(libcst_parameter: LibcstParameter) -> Parameter:
        """Parser a Python parameter."""
        libcst_name: LibcstName = libcst_parameter.name
        name: Name = NameParser.parse_name(libcst_name)

        parameter: Parameter = Parameter(name)
        return parameter

    @staticmethod
    def parse_parameters(libcst_parameters: LibcstParameters) -> ParameterList:
        """Parser Python parameters."""
        parameters: ParameterList = [
            ParameterParser.parse_parameter(libcst_parameter)
            for libcst_parameter in libcst_parameters.params
        ]
        return parameters
