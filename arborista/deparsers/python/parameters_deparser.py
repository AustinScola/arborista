"""A deparser for Python parameters."""
from typing import List

from arborista.deparser import Deparser
from arborista.deparsers.python.positional_parameter_deparser import PositionalParameterDeparser
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.positional_parameter import PositionalParameter


class ParametersDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python parameters."""
    @staticmethod
    def deparse_parameters(parameters: Parameters) -> str:
        """Deparse Python parameters."""
        string: str

        positional_parameters: List[PositionalParameter] = parameters.positional
        positional_parameters_strings = (
            PositionalParameterDeparser.deparse_positional_parameter(positional_parameter)
            for positional_parameter in positional_parameters)
        positional_parameters_string: str = ', '.join(positional_parameters_strings)

        string = positional_parameters_string

        return string
