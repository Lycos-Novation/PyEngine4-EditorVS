from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class PythonSubNode(BaseNode):
    __identifier__ = "Python"

    NODE_NAME = "Sub"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_input("Left")
        self.add_input("Right")
        self.add_output("Trigger", painter_func=draw_trigger_port)
        self.add_output("Result")
