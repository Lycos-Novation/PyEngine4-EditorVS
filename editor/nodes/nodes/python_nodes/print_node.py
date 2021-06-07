from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class PythonPrintNode(BaseNode):
    __identifier__ = "Python"

    NODE_NAME = "Print"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_input("(Value)")
        self.add_output("Trigger", painter_func=draw_trigger_port)
