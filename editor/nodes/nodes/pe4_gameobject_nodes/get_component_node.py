from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class GOGetComponentNode(BaseNode):
    __identifier__ = "PE4.GameObject"

    NODE_NAME = "Get Component"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_input("GameObject")
        self.add_input("Name")
        self.add_output("Trigger", painter_func=draw_trigger_port)
        self.add_output("Component")
