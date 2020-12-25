"""Transformation for deparsing a module to a string."""
from typing import Optional, cast

from arborista.deparsers.python.module_deparser import ModuleDeparser
from arborista.node import Node, NodeTypeSet
from arborista.nodes.file_system.file import File
from arborista.nodes.python.module import Module
from arborista.nodes.sequences.text.string import String
from arborista.transformation import Transformation
from arborista.transformation_result import TransformationResult


class ModuleToString(Transformation):  # pylint: disable=too-few-public-methods
    """Transformation for deparsing a module to a string."""
    NODE_TYPES: NodeTypeSet = {Module}

    @classmethod
    def maybe_transform(cls, node: Node) -> TransformationResult:
        node.assert_is_type(cls.NODE_TYPES)

        module: Module = cast(Module, node)
        module_string: str = ModuleDeparser.deparse_module(module)
        string: String = String(module_string)

        parent: Optional[Node] = module.parent
        if isinstance(parent, File):
            file_: File = parent
            if file_.contents is module:
                file_.contents = string

        transformation_result: TransformationResult = TransformationResult(string, True, [module])
        return transformation_result
