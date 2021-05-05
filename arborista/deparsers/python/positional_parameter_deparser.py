"""Deparser for a Python positional parameter."""
from arborista.deparser import Deparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.nodes.python.positional_parameter import PositionalParameter


class PositionalParameterDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python positional parameter."""
    @staticmethod
    def deparse_positional_parameter(positional_parameter: PositionalParameter) -> str:
        """Deparse a Python positional parameter."""
        name_string: str = NameDeparser.deparse_name(positional_parameter.name)
        return name_string
