from editor.nodes.core import BaseNode


class GameObjectNode(BaseNode):
    __identifier__ = "PE4.GameObject"

    NODE_NAME = "GameObject"

    def __init__(self):
        super().__init__()
        self.add_output("GameObject")
