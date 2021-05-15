from editor.nodes.core import BaseNode


class TestingNode(BaseNode):
    __identifier__ = "PE4EditorVS"

    NODE_NAME = "Testing Node"

    def __init__(self):
        super().__init__()
        self.add_input("foo", color=(255, 0, 0))
        self.add_output("Bibou")
