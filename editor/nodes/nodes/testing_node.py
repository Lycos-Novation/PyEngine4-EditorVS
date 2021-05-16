from editor.nodes.core import BaseNode


class TestingNode(BaseNode):
    __identifier__ = "Testing"

    NODE_NAME = "Testing Node"

    def __init__(self):
        super().__init__()
        self.add_input("foo", color=(255, 0, 0))
        self.add_output("Bibou")
