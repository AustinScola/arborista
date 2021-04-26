"""A parser for a Python slice."""
from typing import Optional

import libcst

from arborista.nodes.python.expression import Expression
from arborista.nodes.python.slice import Slice
from arborista.parser import Parser

LibcstSlice = libcst.Slice


class SliceParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python slice."""
    @staticmethod
    def parse_slice(libcst_slice: LibcstSlice) -> Slice:
        """Parse a Python slice."""
        from arborista.parsers.python.expression_parser import (  # pylint: disable=import-outside-toplevel
            ExpressionParser, LibcstExpression)

        libcst_start: Optional[LibcstExpression] = libcst_slice.lower
        start: Optional[Expression]
        if libcst_start is not None:
            start = ExpressionParser.parse_expression(libcst_start)
        else:
            start = None

        libcst_end: Optional[LibcstExpression] = libcst_slice.upper
        end: Optional[Expression]
        if libcst_end is not None:
            end = ExpressionParser.parse_expression(libcst_end)
        else:
            end = None

        libcst_step: Optional[LibcstExpression] = libcst_slice.step
        step: Optional[Expression]
        if libcst_step is not None:
            step = ExpressionParser.parse_expression(libcst_step)
        else:
            step = None

        slice_: Slice = Slice(start, end, step)
        return slice_
