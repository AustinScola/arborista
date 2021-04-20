"""Parser for a Python expression."""
import libcst

from arborista.nodes.python.atom import Atom
from arborista.nodes.python.comparison import Comparison
from arborista.nodes.python.expression import Expression
from arborista.parser import Parser
from arborista.parsers.python.atom_parser import AtomParser, LibcstAtom
from arborista.parsers.python.comparison_parser import ComparisonParser, LibcstComparison
from arborista.parsers.python.number_parser import LibcstNumber

LibcstExpression = libcst.BaseExpression


class ExpressionParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python expression statement."""
    @staticmethod
    def parse_expression(libcst_expression: LibcstExpression) -> Expression:
        """Parse a Python expression statement."""
        expression: Expression
        if isinstance(libcst_expression,
                      (LibcstNumber, libcst.SimpleString, libcst.FormattedString)):
            libcst_atom: LibcstAtom = libcst_expression
            atom: Atom = AtomParser.parse_atom(libcst_atom)
            expression = atom
        elif isinstance(libcst_expression, libcst.Comparison):
            libcst_comparison: LibcstComparison = libcst_expression
            comparison: Comparison = ComparisonParser.parse_comparison(libcst_comparison)
            expression = comparison
        else:
            raise NotImplementedError  # pragma: no cover
        return expression
