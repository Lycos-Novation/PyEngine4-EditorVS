from editor.nodes.core import BaseNode


class PythonAttributeNode(BaseNode):
    __identifier__ = "Python"

    NODE_NAME = "Attribute"

    def __init__(self):
        super().__init__()
        self.add_input("Object")
        self.add_input("Name")
        self.add_output("Attribute")
