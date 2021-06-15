from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class MathClampNode(BaseNode):
    __identifier__ = "PE4.Math"

    NODE_NAME = "Clamp"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_input("Value")
        self.add_input("(Mini)")
        self.add_input("(Maxi)")
        self.add_output("Trigger", painter_func=draw_trigger_port)
        self.add_output("Value")
