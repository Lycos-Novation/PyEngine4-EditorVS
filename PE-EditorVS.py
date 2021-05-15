import sys
from PyQt5.QtWidgets import *

from editor.editor_vs import EditorVS


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = EditorVS()

    sys.exit(app.exec_())
