"""Test arborista.deparsers.python.decorator_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.decorator_deparser import DecoratorDeparser
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.decorator import Decorator, Decorators
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.decorator_deparser.DecoratorDeparser inheritance."""
    assert issubclass(DecoratorDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('decorator, indent, expected_string', [
    (Decorator(DottedName(Name('foo'), [])), '', '@foo\n'),
    (Decorator(DottedName(Name('foo'), [])), '\t', '\t@foo\n'),
    (Decorator(DottedName(Name('foo'), [])), '    ', '    @foo\n'),
    (Decorator(DottedName(Name('foo'), []), Arguments()), '', '@foo()\n'),
    (Decorator(DottedName(Name('foo'), []), Arguments([Name('bar')])), '', '@foo(bar)\n'),
    (Decorator(DottedName(Name('foo'), []), Arguments([Name('bar'), Name('baz')])), '', '@foo(bar, baz)\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparser_decorator(decorator: Decorator, indent: str, expected_string: str) -> None:
    """Test arborista.deparsers.python.decorator_deparser.DecoratorDeparser.deparse_decorator."""
    string: str = DecoratorDeparser.deparse_decorator(decorator, indent)

    assert string == expected_string


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('decorators, indent, expected_string', [
    ([], '', ''),
    ([Decorator(DottedName(Name('foo'), [])), Decorator(DottedName(Name('bar'), []))], '', '@foo\n@bar\n'),
    ([Decorator(DottedName(Name('foo'), [])), Decorator(DottedName(Name('bar'), []))], '    ', '    @foo\n    @bar\n'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparser_decorators(decorators: Decorators, indent: str, expected_string: str) -> None:
    """Test arborista.deparsers.python.decorator_deparser.DecoratorDeparser.deparse_decorators."""
    string: str = DecoratorDeparser.deparse_decorators(decorators, indent)

    assert string == expected_string
