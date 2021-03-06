from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class MathDistanceBetweenRectNode(BaseNode):
    __identifier__ = "PE4.Math"

    NODE_NAME = "Distance Between Rects"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_input("Pos")
        self.add_input("Size")
        self.add_input("Pos 2")
        self.add_input("Size 2")
        self.add_output("Trigger", painter_func=draw_trigger_port)
        self.add_output("Distance")
