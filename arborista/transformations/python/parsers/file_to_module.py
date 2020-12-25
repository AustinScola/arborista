"""Transformation for parsing module from a file."""
from typing import cast

from arborista.node import Node, NodeTypeSet
from arborista.nodes.file_system.file import File
from arborista.nodes.python.module import Module
from arborista.nodes.sequences.text.string import String
from arborista.parsers.python.module_parser import ModuleParser
from arborista.transformation import Transformation
from arborista.transformation_result import TransformationResult


class FileToModule(Transformation):  # pylint: disable=too-few-public-methods
    """Transformation for parsing module from a file."""
    NODE_TYPES: NodeTypeSet = {File}

    @classmethod
    def maybe_transform(cls, node: Node) -> TransformationResult:
        node.assert_is_type(cls.NODE_TYPES)

        transformation_result: TransformationResult

        file_: File = cast(File, node)
        contents: Node = file_.contents
        if isinstance(contents, String):
            name = file_.stem

            string: String = contents
            string_value: str = string.value

            module: Module = ModuleParser.parse_module(name, string_value)

            file_.contents = module

            transformation_result = TransformationResult(file_, True, [string])
        else:
            transformation_result = TransformationResult(file_, False, [])

        return transformation_result
