from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class Vec2DistanceNode(BaseNode):
    __identifier__ = "PE4.Vec2"

    NODE_NAME = "Distance"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_input("Vec")
        self.add_input("Vec2")
        self.add_output("Trigger", painter_func=draw_trigger_port)
        self.add_output("Distance")
