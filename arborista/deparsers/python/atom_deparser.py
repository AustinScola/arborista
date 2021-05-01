"""A deparser for a Python atom."""
from arborista.deparser import Deparser
from arborista.deparsers.python.name_deparser import NameDeparser
from arborista.deparsers.python.string_deparser import StringDeparser
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.name import Name
from arborista.nodes.python.string import String


class AtomDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for a Python atom."""
    @staticmethod
    def deparse_atom(atom: Atom) -> str:
        """Deparse a Python atom."""
        string: str

        if isinstance(atom, String):
            string_node: String = atom
            string = StringDeparser.deparse_string(string_node)
        elif isinstance(atom, Name):
            name: Name = atom
            string = NameDeparser.deparse_name(name)
        else:
            raise NotImplementedError  # pragma: no cover

        return string
