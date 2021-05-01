"""Deparser for a Python comparison operator."""
from arborista.deparser import Deparser
from arborista.deparsers.python.equals_deparser import EqualsDeparser
from arborista.deparsers.python.greater_than_deparser import GreaterThanDeparser
from arborista.deparsers.python.greater_than_or_equals_deparser import GreaterThanOrEqualsDeparser
from arborista.deparsers.python.in_deparser import InDeparser
from arborista.deparsers.python.is_deparser import IsDeparser
from arborista.deparsers.python.is_not_deparser import IsNotDeparser
from arborista.deparsers.python.less_greater_than_deparser import LessGreaterThanDeparser
from arborista.deparsers.python.less_than_deparser import LessThanDeparser
from arborista.deparsers.python.less_than_or_equals_deparser import LessThanOrEqualsDeparser
from arborista.deparsers.python.not_equals_deparser import NotEqualsDeparser
from arborista.deparsers.python.not_in_deparser import NotInDeparser
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.equals import Equals
from arborista.nodes.python.greater_than import GreaterThan
from arborista.nodes.python.greater_than_or_equals import GreaterThanOrEquals
from arborista.nodes.python.in_ import In
from arborista.nodes.python.is_ import Is
from arborista.nodes.python.is_not import IsNot
from arborista.nodes.python.less_greater_than import LessGreaterThan
from arborista.nodes.python.less_than import LessThan
from arborista.nodes.python.less_than_or_equals import LessThanOrEquals
from arborista.nodes.python.not_equals import NotEquals
from arborista.nodes.python.not_in import NotIn


class ComparisonOperatorDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python comparison operator."""
    @staticmethod
    def deparse_comparison_operator(comparison_operator: ComparisonOperator) -> str:
        """Deparse a Python comparison operator."""
        string: str

        if isinstance(comparison_operator, LessThan):
            less_than: LessThan = comparison_operator
            string = LessThanDeparser.deparse_less_than(less_than)
        elif isinstance(comparison_operator, GreaterThan):
            greater_than: GreaterThan = comparison_operator
            string = GreaterThanDeparser.deparse_greater_than(greater_than)
        elif isinstance(comparison_operator, Equals):
            equals: Equals = comparison_operator
            string = EqualsDeparser.deparse_equals(equals)
        elif isinstance(comparison_operator, GreaterThanOrEquals):
            greater_than_or_equals: GreaterThanOrEquals = comparison_operator
            string = GreaterThanOrEqualsDeparser.deparse_greater_than_or_equals(
                greater_than_or_equals)
        elif isinstance(comparison_operator, LessThanOrEquals):
            less_than_or_equals: LessThanOrEquals = comparison_operator
            string = LessThanOrEqualsDeparser.deparse_less_than_or_equals(less_than_or_equals)
        elif isinstance(comparison_operator, LessGreaterThan):
            less_greater_than: LessGreaterThan = comparison_operator
            string = LessGreaterThanDeparser.deparse_less_greater_than(less_greater_than)
        elif isinstance(comparison_operator, NotEquals):
            not_equals: NotEquals = comparison_operator
            string = NotEqualsDeparser.deparse_not_equals(not_equals)
        elif isinstance(comparison_operator, In):
            in_: In = comparison_operator
            string = InDeparser.deparse_in(in_)
        elif isinstance(comparison_operator, NotIn):
            not_in: NotIn = comparison_operator
            string = NotInDeparser.deparse_not_in(not_in)
        elif isinstance(comparison_operator, Is):
            is_: Is = comparison_operator
            string = IsDeparser.deparse_is(is_)
        elif isinstance(comparison_operator, IsNot):
            is_not: IsNot = comparison_operator
            string = IsNotDeparser.deparse_is_not(is_not)
        else:
            raise NotImplementedError  # pragma: no cover

        return string
