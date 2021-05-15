from PyQt5.QtWidgets import QWidget, QVBoxLayout

from editor.nodes.core import NodeGraph, setup_context_menu, BackdropNode
from editor.nodes.testing_node import TestingNode


class NodeEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.graph = NodeGraph()
        setup_context_menu(self.graph)

        self.graph.register_node(BackdropNode)
        self.graph.register_node(TestingNode)

        node1 = self.graph.create_node('PE4EditorVS.TestingNode', name="TEST 1")
        node2 = self.graph.create_node('PE4EditorVS.TestingNode', name="TEST 2")
        node3 = self.graph.create_node('PE4EditorVS.TestingNode', name="TEST 3")
        back = self.graph.create_node('nodeGraphQt.nodes.BackdropNode', name='Backdrop')

        back.wrap_nodes([node1, node2])

        node1.set_input(0, node2.output(0))

        self.graph.auto_layout_nodes()

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.layout.addWidget(self.graph.widget)
