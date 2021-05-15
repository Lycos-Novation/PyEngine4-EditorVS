from PyQt5.QtWidgets import *

from editor.nodes.node_editor import NodeEditor


class EditorVS(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(200, 200, 800, 600)
        self.node_editor = NodeEditor(self)
        self.setCentralWidget(self.node_editor)

        self.setWindowTitle("PyEngine 4 - Visual Scripting Editor")
        self.show()
