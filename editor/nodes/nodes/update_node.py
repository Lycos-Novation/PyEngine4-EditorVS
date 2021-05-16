from editor.nodes.core import BaseNode


class UpdateNode(BaseNode):
    __identifier__ = "Events"

    NODE_NAME = "Update"

    def __init__(self):
        super().__init__()
        self.add_output("Trigger")
        self.add_output("DeltaTime")
