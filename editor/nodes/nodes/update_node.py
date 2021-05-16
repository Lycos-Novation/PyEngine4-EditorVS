from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class UpdateNode(BaseNode):
    __identifier__ = "Events"

    NODE_NAME = "Update"

    def __init__(self):
        super().__init__()
        self.add_output("Trigger", painter_func=draw_trigger_port)
        self.add_output("DeltaTime")
