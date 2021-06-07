from editor.nodes.core import BaseNode


class PythonNoneNode(BaseNode):
    __identifier__ = "Python"

    NODE_NAME = "None"

    def __init__(self):
        super().__init__()
        self.add_output("None")
