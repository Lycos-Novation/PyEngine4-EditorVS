from editor.nodes.core import BaseNode


class PythonSelfNode(BaseNode):
    __identifier__ = "Python"

    NODE_NAME = "Self"

    def __init__(self):
        super().__init__()
        self.add_output("Self")
