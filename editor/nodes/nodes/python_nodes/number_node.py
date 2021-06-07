from editor.nodes.core import BaseNode


class PythonNumberNode(BaseNode):
    __identifier__ = "Python"

    NODE_NAME = "Number"

    def __init__(self):
        super().__init__()
        self.add_text_input("Number")
        self.add_output("")
