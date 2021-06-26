from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class ColorFromColorNode(BaseNode):
    __identifier__ = "PE4.Color"

    NODE_NAME = "From Color"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_input("Color")
        self.add_output("Trigger", painter_func=draw_trigger_port)
        self.add_output("Color")
