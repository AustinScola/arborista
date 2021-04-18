"""A parser for a Python import from statement."""
from typing import Optional, Union

import libcst

from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.grouped_name_as_names import GroupedNameAsNames
from arborista.nodes.python.import_from import ImportFrom
from arborista.nodes.python.name import Name
from arborista.nodes.python.name_as_names import NameAsNames
from arborista.nodes.python.relative_dotted_name import RelativeDottedName
from arborista.nodes.python.star import Star
from arborista.parser import Parser
from arborista.parsers.python.dotted_name_parser import DottedNameParser, LibcstDottedName
from arborista.parsers.python.name_as_names_parser import LibcstNameAsNames, NameAsNamesParser
from arborista.parsers.python.name_parser import LibcstName, NameParser

Source = Union[DottedName, RelativeDottedName]
Target = Union[Star, GroupedNameAsNames, NameAsNames]

LibcstImportFrom = libcst.ImportFrom


class ImportFromParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python import from statement."""
    @staticmethod
    def parse_import_from(libcst_import_from: LibcstImportFrom) -> ImportFrom:
        """Parse an import from statement."""
        source: Source
        dotted_name: Optional[DottedName]
        if isinstance(libcst_import_from.module, LibcstName):
            libcst_name: LibcstName = libcst_import_from.module
            name: Name = NameParser.parse_name(libcst_name)
            dotted_name = DottedName(name, [])
            if libcst_import_from.relative:
                source = RelativeDottedName(len(libcst_import_from.relative), dotted_name)
            else:
                source = dotted_name
        else:
            libcst_dotted_name: Optional[LibcstDottedName] = libcst_import_from.module
            if libcst_dotted_name is None:
                source = RelativeDottedName(len(libcst_import_from.relative), None)
            else:
                dotted_name = DottedNameParser.parse_dotted_name(libcst_dotted_name)

                if libcst_import_from.relative:
                    source = RelativeDottedName(len(libcst_import_from.relative), dotted_name)
                else:
                    source = dotted_name

        target: Target

        if isinstance(libcst_import_from.names, libcst.ImportStar):
            target = Star()
        else:
            libcst_name_as_names: LibcstNameAsNames = libcst_import_from.names
            name_as_names: NameAsNames = NameAsNamesParser.parse_name_as_names(libcst_name_as_names)

            if libcst_import_from.lpar and libcst_import_from.rpar:
                target = GroupedNameAsNames(name_as_names)
            else:
                target = name_as_names

        import_from: ImportFrom = ImportFrom(source, target)
        return import_from
