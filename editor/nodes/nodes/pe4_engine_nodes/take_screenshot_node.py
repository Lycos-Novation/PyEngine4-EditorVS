from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class TakeScreenshotNode(BaseNode):
    __identifier__ = "PE4.Engine"

    NODE_NAME = "Take Screenshot"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_input("Engine")
        self.add_input("(Path)")
        self.add_input("(Position)")
        self.add_input("(Size)")
        self.add_output("Trigger", painter_func=draw_trigger_port)
