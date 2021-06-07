from editor.nodes.core import BaseNode

from editor.nodes.utils import draw_trigger_port


class SceneAddGameObjectsNode(BaseNode):
    __identifier__ = "PE4.Scene"

    NODE_NAME = "Add GameObjects"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger", painter_func=draw_trigger_port)
        self.add_input("Scene")
        self.add_input("GameObjects")
        self.add_output("Trigger", painter_func=draw_trigger_port)
