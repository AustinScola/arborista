"""A parser for a Python dotted name as another name."""
from typing import Optional, Union

import libcst

from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.dotted_name_as_name import DottedNameAsName
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.dotted_name_parser import DottedNameParser, LibcstDottedName
from arborista.parsers.python.name_parser import LibcstName, NameParser

LibcstDottedNameAsName = libcst.ImportAlias


class DottedNameAsNameParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python dotted name as another name."""
    @staticmethod
    def parse_dotted_name_as_name(
            libcst_dotted_name_as_name: LibcstDottedNameAsName) -> DottedNameAsName:
        """Parser a Python dotted name."""
        dotted_name: DottedName
        if isinstance(libcst_dotted_name_as_name.name, LibcstName):
            first_name: Name = NameParser.parse_name(libcst_dotted_name_as_name.name)
            dotted_name = DottedName(first_name, [])
        else:
            libcst_dotted_name: LibcstDottedName = libcst_dotted_name_as_name.name
            dotted_name = DottedNameParser.parse_dotted_name(libcst_dotted_name)

        name: Optional[Name]
        if isinstance(libcst_dotted_name_as_name.asname, libcst.AsName):
            libcst_as_name_name: Union[LibcstName, libcst.Tuple,
                                       libcst.List] = libcst_dotted_name_as_name.asname.name
            if isinstance(libcst_as_name_name, LibcstName):
                name = NameParser.parse_name(libcst_as_name_name)
            else:
                raise NotImplementedError  # pragma: no cover
        else:
            name = None

        dotted_name_as_name: DottedNameAsName = DottedNameAsName(dotted_name, name)
        return dotted_name_as_name
