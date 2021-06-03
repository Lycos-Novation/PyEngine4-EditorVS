from editor.nodes.core import BaseNode


class EngineNode(BaseNode):
    __identifier__ = "PE4.Engine"

    NODE_NAME = "Engine"

    def __init__(self):
        super().__init__()
        self.add_output("Engine")
