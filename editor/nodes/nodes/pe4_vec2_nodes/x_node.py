from editor.nodes.core import BaseNode


class Vec2XNode(BaseNode):
    __identifier__ = "PE4.Vec2"

    NODE_NAME = "X"

    def __init__(self):
        super().__init__()
        self.add_input("Vec2")
        self.add_output("X")
