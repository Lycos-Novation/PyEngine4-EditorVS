from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class Vec2ZeroNode(BaseNode):
    __identifier__ = "PE4.Vec2"

    NODE_NAME = "Zero"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_output("Trigger", painter_func=draw_trigger_port)
        self.add_output("Vec2")
