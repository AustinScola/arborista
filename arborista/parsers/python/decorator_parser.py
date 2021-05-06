"""A Parser for Python decorators."""
from typing import Optional, Sequence

import libcst

from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.decorator import Decorator, Decorators
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.arguments_parser import ArgumentsParser, LibcstArguments
from arborista.parsers.python.dotted_name_parser import DottedNameParser, LibcstDottedName
from arborista.parsers.python.function_call_parser import LibcstFunctionCall
from arborista.parsers.python.name_parser import LibcstName, NameParser

LibcstDecorator = libcst.Decorator
LibcstDecorators = Sequence[LibcstDecorator]


class DecoratorParser(Parser):
    """A Parser for Python decorators."""
    @staticmethod
    def parse_decorator(libcst_decorator: LibcstDecorator) -> Decorator:
        """Parse a Python decorator."""
        dotted_name: DottedName
        arguments: Optional[Arguments]

        if isinstance(libcst_decorator.decorator, LibcstName):
            libcst_name: LibcstName = libcst_decorator.decorator
            name: Name = NameParser.parse_name(libcst_name)
            dotted_name = DottedName(name, [])
            arguments = None
        elif isinstance(libcst_decorator.decorator, LibcstDottedName):
            libcst_dotted_name: LibcstDottedName = libcst_decorator.decorator
            dotted_name = DottedNameParser.parse_dotted_name(libcst_dotted_name)
            arguments = None
        else:
            libcst_function_call: LibcstFunctionCall = libcst_decorator.decorator
            if isinstance(libcst_function_call.func, LibcstName):
                libcst_name = libcst_function_call.func
                name = NameParser.parse_name(libcst_name)
                dotted_name = DottedName(name, [])
            elif isinstance(libcst_function_call.func, LibcstDottedName):
                libcst_dotted_name = libcst_function_call.func
                dotted_name = DottedNameParser.parse_dotted_name(libcst_dotted_name)
            else:
                raise ValueError('Libcst function call must have a name or dotted name as the function.')  # pragma: no cover  # pylint: disable=line-too-long, useless-suppression

            libcst_arguments: LibcstArguments = libcst_function_call.args
            arguments = ArgumentsParser.parse_arguments(libcst_arguments)

        decorator: Decorator = Decorator(dotted_name, arguments)

        return decorator

    @staticmethod
    def parse_decorators(libcst_decorators: LibcstDecorators) -> Decorators:
        """Parse a Python decorators."""
        decorators = [
            DecoratorParser.parse_decorator(libcst_decorator)
            for libcst_decorator in libcst_decorators
        ]
        return decorators
