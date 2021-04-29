"""A deparser for Python dotted names."""
from arborista.deparser import Deparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name, Names


class DottedNameDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for Python dotted names."""
    @staticmethod
    def deparse_dotted_name(dotted_name: DottedName) -> str:
        """Deparser a Python dotted name."""
        string: str

        first_name: Name = dotted_name.first_name
        first_string: str = NameDeparser.deparse_name(first_name)

        rest_of_names: Names = dotted_name.rest_of_names
        rest_of_names_strings = (NameDeparser.deparse_name(name) for name in rest_of_names)

        string = first_string + ''.join(f'.{name_string}' for name_string in rest_of_names_strings)

        return string
