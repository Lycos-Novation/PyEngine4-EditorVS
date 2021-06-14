from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class Vec2SetCoordsNode(BaseNode):
    __identifier__ = "PE4.Vec2"

    NODE_NAME = "Set Coords"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_input("Vec2")
        self.add_input("X")
        self.add_input("Y")
        self.add_output("Trigger", painter_func=draw_trigger_port)
