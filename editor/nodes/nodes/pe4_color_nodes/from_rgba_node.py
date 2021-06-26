from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class ColorFromRGBANode(BaseNode):
    __identifier__ = "PE4.Color"

    NODE_NAME = "From RGBA"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_input("Red")
        self.add_input("Green")
        self.add_input("Blue")
        self.add_input("Alpha")
        self.add_output("Trigger", painter_func=draw_trigger_port)
        self.add_output("Color")
