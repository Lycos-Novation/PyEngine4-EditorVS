from editor.nodes.core import BaseNode


class PythonIdentifierNode(BaseNode):
    __identifier__ = "Python"

    NODE_NAME = "Identifier"

    def __init__(self):
        super().__init__()
        self.add_text_input("Name")
        self.add_output("")
