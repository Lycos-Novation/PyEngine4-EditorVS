from editor.nodes.core import BaseNode


class Vec2YNode(BaseNode):
    __identifier__ = "PE4.Vec2"

    NODE_NAME = "Y"

    def __init__(self):
        super().__init__()
        self.add_input("Vec2")
        self.add_output("Y")
