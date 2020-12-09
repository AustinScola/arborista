"""Deparser for a Python parameter."""
from arborista.deparser import Deparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.nodes.python.parameter import Parameter


class ParameterDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python parameter."""
    @staticmethod
    def deparse_parameter(parameter: Parameter) -> str:
        """Deparse a Python parameter."""
        name_string: str = NameDeparser.deparse_name(parameter.name)
        return name_string
