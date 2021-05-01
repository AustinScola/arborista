"""A deparser for a Python expression."""
from arborista.deparser import Deparser
from arborista.deparsers.python.atom_deparser import AtomDeparser
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.expression import Expression


class ExpressionDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for a Python expression."""
    @staticmethod
    def deparse_expression(expression: Expression) -> str:
        """Deparse a Python expression."""
        string: str

        if isinstance(expression, Atom):
            atom = expression
            string = AtomDeparser.deparse_atom(atom)
        else:
            raise NotImplementedError  # pragma: no cover

        return string
