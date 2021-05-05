"""Parser for a Python positional_parameter."""
import libcst

from arborista.nodes.python.name import Name
from arborista.nodes.python.positional_parameter import PositionalParameter
from arborista.parser import Parser
from arborista.parsers.python.name_parser import LibcstName, NameParser

LibcstPositionalParameter = libcst.Param
LibcstPositionalParameters = libcst.Parameters


class PositionalParameterParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python positional_parameter."""
    @staticmethod
    def parse_positional_parameter(
            libcst_positional_parameter: LibcstPositionalParameter) -> PositionalParameter:
        """Parser a Python positional_parameter."""
        libcst_name: LibcstName = libcst_positional_parameter.name
        name: Name = NameParser.parse_name(libcst_name)

        positional_parameter: PositionalParameter = PositionalParameter(name)
        positional_parameter.set_parent_in_children()

        return positional_parameter
