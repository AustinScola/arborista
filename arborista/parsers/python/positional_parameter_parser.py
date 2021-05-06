"""Parser for a Python positional_parameter."""
from typing import Optional

import libcst

from arborista.nodes.python.expression import Expression
from arborista.nodes.python.name import Name
from arborista.nodes.python.positional_parameter import PositionalParameter
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression
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

        annotation: Optional[Expression]
        if libcst_positional_parameter.annotation is None:
            annotation = None
        else:
            libcst_annotation: LibcstExpression = libcst_positional_parameter.annotation.annotation
            annotation = ExpressionParser.parse_expression(libcst_annotation)

        default: Optional[Expression]
        if libcst_positional_parameter.default is None:
            default = None
        else:
            libcst_default: LibcstExpression = libcst_positional_parameter.default
            default = ExpressionParser.parse_expression(libcst_default)

        positional_parameter: PositionalParameter = PositionalParameter(name, annotation, default)
        positional_parameter.set_parent_in_children()

        return positional_parameter
