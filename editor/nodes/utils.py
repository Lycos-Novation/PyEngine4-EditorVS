from PyQt5.QtWidgets import QFileDialog
import ast

from editor.nodes.core import setup_context_menu
from editor.nodes.ast_parser import parse


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

