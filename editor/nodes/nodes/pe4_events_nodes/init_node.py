from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class InitNode(BaseNode):
    __identifier__ = "PE4.Events"

    NODE_NAME = "Init"

    def __init__(self):
        super().__init__()
        self.add_output("Trigger", painter_func=draw_trigger_port)
