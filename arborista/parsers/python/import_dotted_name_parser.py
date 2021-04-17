"""A Parser for a Python import dotted name."""
import libcst

from arborista.nodes.python.dotted_name_as_names import DottedNameAsNames
from arborista.nodes.python.import_dotted_name import ImportDottedName
from arborista.parser import Parser
from arborista.parsers.python.dotted_name_as_names_parser import (DottedNameAsNamesParser,
                                                                  LibcstDottedNameAsNames)

LibcstImportDottedName = libcst.Import


class ImportDottedNameParser(Parser):  # pylint: disable=too-few-public-methods
    """A Parser for a Python import dotted name."""
    @staticmethod
    def parse_import_dotted_name(
            libcst_import_dotted_name: LibcstImportDottedName) -> ImportDottedName:
        """Parse a Python import dotted name."""
        libcst_dotted_name_as_names: LibcstDottedNameAsNames = list(libcst_import_dotted_name.names)
        dotted_name_as_names: DottedNameAsNames = \
            DottedNameAsNamesParser.parse_dotted_name_as_names(libcst_dotted_name_as_names)

        import_dotted_name: ImportDottedName = ImportDottedName(dotted_name_as_names)
        return import_dotted_name
