from editor.nodes.core import BaseNode


class LiteralNode(BaseNode):
    __identifier__ = "Python"

    NODE_NAME = "Literal"

    def __init__(self):
        super().__init__()
        self.add_text_input("Text")
        self.add_output("")
