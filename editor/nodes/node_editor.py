from PyQt5.QtWidgets import QWidget, QVBoxLayout

from editor.nodes.core import NodeGraph, BackdropNode
from editor.nodes.utils import context_menu
from editor.nodes import nodes


class NodeEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.graph = NodeGraph()

        for i in nodes.nodes:
            self.graph.register_node(i)
        self.graph.register_node(BackdropNode)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.layout.addWidget(self.graph.widget)
        context_menu(self.graph)
