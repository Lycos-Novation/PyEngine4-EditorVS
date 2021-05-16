from editor.nodes.core import BaseNode


class PrintNode(BaseNode):
    __identifier__ = "Python"

    NODE_NAME = "Print"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger")
        self.add_input("Value")
        self.add_output("Trigger")
