from editor.nodes.core import BaseNode


class GetComponentNode(BaseNode):
    __identifier__ = "PE4"

    NODE_NAME = "GetComponent"

    def __init__(self):
        super().__init__()
        self.add_input("Trigger")
        self.add_input("Name")
        self.add_output("Trigger")
        self.add_output("Component")
