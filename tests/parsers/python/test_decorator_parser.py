"""Test arborista.parsers.python.decorator_parser."""
from typing import Sequence

import libcst
import pytest

from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.decorator import Decorator, Decorators
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.decorator_parser import (DecoratorParser, LibcstDecorator,
                                                       LibcstDecorators)


def test_libcst_decorator() -> None:
    """Test arborista.parsers.python.decorators_parser.LibcstDecorator."""
    assert LibcstDecorator == libcst.Decorator


def test_libcst_decorators() -> None:
    """Test arborista.parsers.python.decorators_parser.LibcstDecorators."""
    assert isinstance(LibcstDecorators, type(Sequence))
    assert LibcstDecorators.__args__ == (LibcstDecorator, )  # type: ignore[attr-defined]


def test_inheritance() -> None:
    """Test arborista.parsers.python.decorator_parser.DecoratorParser inheritance."""
    assert issubclass(DecoratorParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_decorator, expected_decorator', [
    (libcst.Decorator(libcst.Name('bar')), Decorator(DottedName(Name('bar'), []))),
    (libcst.Decorator(libcst.Attribute(libcst.Name('foo'), libcst.Name('bar'))), Decorator(DottedName(Name('foo'), [Name('bar')]))),
    (libcst.Decorator(libcst.Call(libcst.Name('foo'), [])), Decorator(DottedName(Name('foo'), []), Arguments())),
    (libcst.Decorator(libcst.Call(libcst.Name('foo'), [libcst.Arg(libcst.Name('bar'))])), Decorator(DottedName(Name('foo'), []), Arguments([Name('bar')]))),
    (libcst.Decorator(libcst.Call(libcst.Attribute(libcst.Name('foo'), libcst.Name('bar')), [libcst.Arg(libcst.Name('baz'))])), Decorator(DottedName(Name('foo'), [Name('bar')]), Arguments([Name('baz')]))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_decorator(libcst_decorator: LibcstDecorator, expected_decorator: Decorator) -> None:
    """Test arborista.parsers.python.decorators_parser.DecoratorParser.parse_decorator."""
    decorator: Decorator = DecoratorParser.parse_decorator(libcst_decorator)

    assert decorator == expected_decorator


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_decorators, expected_decorators', [
    ([], []),
    ([libcst.Decorator(libcst.Name('foo'))], [Decorator(DottedName(Name('foo'), []))]),
    ([libcst.Decorator(libcst.Name('foo')), libcst.Decorator(libcst.Name('bar'))], [Decorator(DottedName(Name('foo'), [])), Decorator(DottedName(Name('bar'), []))]),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_decorators(libcst_decorators: LibcstDecorators,
                          expected_decorators: Decorators) -> None:
    """Test arborista.parsers.python.decorators_parser.DecoratorParser.parse_decorators."""
    decorators: Decorators = DecoratorParser.parse_decorators(libcst_decorators)

    assert decorators == expected_decorators
