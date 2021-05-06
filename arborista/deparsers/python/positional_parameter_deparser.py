"""Deparser for a Python positional parameter."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.expression_deparser import ExpressionDeparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.positional_parameter import PositionalParameter


class PositionalParameterDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python positional parameter."""
    @staticmethod
    def deparse_positional_parameter(positional_parameter: PositionalParameter) -> str:
        """Deparse a Python positional parameter."""
        string: str

        name_string: str = NameDeparser.deparse_name(positional_parameter.name)

        string = name_string

        annotation: Optional[Expression] = positional_parameter.annotation
        if annotation is not None:
            annotation_string = ExpressionDeparser.deparse_expression(annotation)
            string = name_string + ': ' + annotation_string

        default: Optional[Expression] = positional_parameter.default
        if default is not None:
            default_string = ExpressionDeparser.deparse_expression(default)
            string += ' = ' + default_string

        return string
