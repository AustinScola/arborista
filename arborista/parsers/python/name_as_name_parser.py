"""A parser for a Python name as another name."""
from typing import Optional

import libcst

from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_name import NameAsName
from arborista.parser import Parser
from arborista.parsers.python.dotted_name_parser import LibcstDottedName
from arborista.parsers.python.name_parser import LibcstName, NameParser

LibcstNameAsName = libcst.ImportAlias


class NameAsNameParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python name as another name."""
    @staticmethod
    def parse_name_as_name(libcst_name_as_name: LibcstNameAsName) -> NameAsName:
        """Parse a Python name as another name."""
        if isinstance(libcst_name_as_name.name, LibcstDottedName):
            raise NotImplementedError  # pragma: no cover
        libcst_name: LibcstName = libcst_name_as_name.name
        name: Name = NameParser.parse_name(libcst_name)

        new_name: Optional[Name]
        if libcst_name_as_name.asname is not None:
            if not isinstance(libcst_name_as_name.asname.name, LibcstName):
                raise NotImplementedError  # pragma: no cover
            libcst_new_name: LibcstName = libcst_name_as_name.asname.name
            new_name = NameParser.parse_name(libcst_new_name)
        else:
            new_name = None

        name_as_name: NameAsName = NameAsName(name, new_name)
        return name_as_name
