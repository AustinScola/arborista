"""A parser for Python dotted names."""
from typing import List

import libcst

from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import LibcstExpression
from arborista.parsers.python.name_parser import LibcstName, NameParser

LibcstDottedName = libcst.Attribute


class DottedNameParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for Python dotted names."""
    @staticmethod
    def parse_dotted_name(libcst_dotted_name: LibcstDottedName) -> DottedName:
        """Parser a Python dotted name."""
        first_name: Name
        rest_of_names: List[Name] = []
        while True:
            libcst_name: LibcstName = libcst_dotted_name.attr
            name: Name = NameParser.parse_name(libcst_name)
            rest_of_names = [name] + rest_of_names

            libcst_value: LibcstExpression = libcst_dotted_name.value
            if isinstance(libcst_value, LibcstName):
                libcst_name = libcst_value
                first_name = NameParser.parse_name(libcst_name)
                break
            if isinstance(libcst_value, LibcstDottedName):
                libcst_dotted_name = libcst_value
            else:
                raise ValueError(f'Dotted names should have a dotted name of a name as the value not a {type(libcst_value)}')  # pragma: no cover  # pylint: disable=line-too-long, useless-suppression

        dotted_name: DottedName = DottedName(first_name, rest_of_names)
        return dotted_name
