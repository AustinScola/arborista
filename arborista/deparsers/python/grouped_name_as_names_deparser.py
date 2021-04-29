"""A deparser for Python grouped name as names."""
from arborista.deparser import Deparser
from arborista.deparsers.python.name_as_names_deparser import NameAsNamesDeparser
from arborista.nodes.python.grouped_name_as_names import GroupedNameAsNames
from arborista.nodes.python.name_as_names import NameAsNames


class GroupedNameAsNamesDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python grouped name as names."""
    @staticmethod
    def deparse_grouped_name_as_names(grouped_name_as_names: GroupedNameAsNames) -> str:
        """Deparser a Python grouped name as names."""
        string: str

        name_as_names: NameAsNames = grouped_name_as_names.name_as_names
        name_as_names_string = NameAsNamesDeparser.deparse_name_as_names(name_as_names)

        string = f'({name_as_names_string})'

        return string
