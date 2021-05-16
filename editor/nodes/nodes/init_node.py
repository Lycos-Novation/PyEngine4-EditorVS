from editor.nodes.core import BaseNode


class InitNode(BaseNode):
    __identifier__ = "Events"

    NODE_NAME = "Init"

    def __init__(self):
        super().__init__()
        self.add_output("Trigger")
