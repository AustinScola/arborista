"""A deparser for a Python slice."""
from typing import Optional

from arborista.deparser import Deparser
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.slice import Slice


class SliceDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for a Python slice."""
    @staticmethod
    def deparse_slice(slice_: Slice) -> str:
        """Deparse a Python slice."""
        from arborista.deparsers.python.expression_deparser import \
            ExpressionDeparser  # pylint: disable=import-outside-toplevel

        start: Optional[Expression] = slice_.start
        start_string: str
        if start is None:
            start_string = ''
        else:
            start_string = ExpressionDeparser.deparse_expression(start)

        end: Optional[Expression] = slice_.end
        end_string: str
        if end is None:
            end_string = ''
        else:
            end_string = ExpressionDeparser.deparse_expression(end)

        string = start_string + ':' + end_string

        step: Optional[Expression] = slice_.step
        step_string: str
        if step is not None:
            step_string = ExpressionDeparser.deparse_expression(step)
            string += ':' + step_string

        return string
