from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class EventsStartNode(BaseNode):
    __identifier__ = "PE4.Events"

    NODE_NAME = "Start"

    def __init__(self):
        super().__init__()
        self.add_output("Trigger", painter_func=draw_trigger_port)
