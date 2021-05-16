from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QTransform, QPolygonF, QColor, QPen
from PyQt5.QtCore import QPointF, Qt
import ast

from editor.nodes.core import setup_context_menu
from editor.nodes.ast_parser import parse


def draw_trigger_port(painter, rect, info):
    painter.save()

    size = int(rect.height() / 2)
    triangle = QPolygonF()
    triangle.append(QPointF(-size, -size))
    triangle.append(QPointF(size, 0))
    triangle.append(QPointF(-size, size))

    transform = QTransform()
    transform.translate(rect.center().x(), rect.center().y())
    port_poly = transform.map(triangle)

    if info["hovered"]:
        color = QColor(17, 43, 82)
        border_color = QColor(136, 255, 35)
    elif info["connected"]:
        color = QColor(14, 45, 59)
        border_color = QColor(107, 166, 193)
    else:
        color = QColor(*info["color"])
        border_color = QColor(*info["border_color"])

    pen = QPen(border_color, 1.8)
    pen.setJoinStyle(Qt.MiterJoin)

    painter.setPen(pen)
    painter.setBrush(color)
    painter.drawPolygon(port_poly)

    painter.restore()


def context_menu(graph):
    menu = graph.get_context_menu('graph')

    pe4_menu = menu.add_menu("&PyEngine 4")

    pe4_menu.add_command('Open Script...', _open_python)
    pe4_menu.add_command('Export Script...', lambda x: print("OP"))

    setup_context_menu(graph)

    with open("examples/paddle_script.py", "r") as f:
        ast_module = ast.parse(f.read())
        print(ast.dump(ast_module, indent=4))
        parse(ast_module, graph)


def _open_python(graph):
    file = QFileDialog.getOpenFileName(graph.viewer(), "Open Python Script", filter="Python Script (*.py)")
    if len(file[0]):
        with open(file[0], "r") as f:
            parse(ast.parse(f.read()), graph)

