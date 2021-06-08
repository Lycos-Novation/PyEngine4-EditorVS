import os

from editor.nodes.generator.python import *
from editor.nodes.generator.pe4_gameobject import *
from editor.nodes.generator.pe4_engine import *
from editor.nodes.generator.pe4_scene import *


def generate(file, graph):
    with open(os.path.join("editor", "res", "template.txt"), "r") as f:
        template = f.read()

    template = template \
        .replace("{NAME}", os.path.basename(file).split(".")[0]) \
        .replace("{TITLE_NAME}", os.path.basename(file).split(".")[0].title())

    init = graph.get_node_by_name("Init")
    if init is not None:
        if len(init.connected_output_nodes()[init.output(0)]):
            template = template.replace("{INIT_BODY}",
                                        generate_functions(init.connected_output_nodes()[init.output(0)][0]))
        else:
            template = template.replace("{INIT_BODY}", "")
    else:
        template = template.replace("{INIT_BODY}", "")

    update = graph.get_node_by_name("Update")
    if update is not None:
        if len(update.connected_output_nodes()[update.output(0)]):
            template = template.replace("{FUNCTIONS}", "    def update(self, deltatime):\n" +
                                        generate_functions(update.connected_output_nodes()[update.output(0)][0]) +
                                        "\n\n{FUNCTIONS}")
        else:
            template = template.replace("{FUNCTIONS}", "    def update(self, deltatime):\n        pass\n\n{FUNCTIONS}")

    template = template.replace("{FUNCTIONS}", "")

    with open(file, "w") as f:
        f.write(template)


def generate_functions(function_node, indent=4):
    lines = []
    while function_node is not None:
        line, function_node = generate_expression(function_node, 8)
        lines.append(line)
    return "\n".join(lines)


def generate_expression(expr_node, indent=0):
    if expr_node.type_ == "PE4.GameObject.GOGetComponentNode":
        line, expr_node = generate_go_getcomponent(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.GameObject.GOAddChildNode":
        line, expr_node = generate_go_addchild(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.GameObject.GOAddComponentNode":
        line, expr_node = generate_go_addcomponent(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.GameObject.GOGameObjectNode":
        line, expr_node = "self.game_object", None

    elif expr_node.type_ == "PE4.Scene.SceneAddGameObjectNode":
        line, expr_node = generate_scene_addgameobject(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Scene.SceneAddGameObjectsNode":
        line, expr_node = generate_scene_addgameobjects(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Scene.SceneGetGameObjectNode":
        line, expr_node = generate_scene_getgameobject(expr_node, indent, generate_expression)

    elif expr_node.type_ == "PE4.Engine.EngineTakeScreenshotNode":
        line, expr_node = generate_engine_takescreenshot(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Engine.EngineGetGameSizeNode":
        line, expr_node = generate_engine_getgamesize(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Engine.EngineStopGameNode":
        line, expr_node = generate_engine_stopgame(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Engine.EngineGetCurrentSceneNode":
        line, expr_node = generate_engine_getcurrentscene(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Engine.EngineGetGameObjectNode":
        line, expr_node = generate_engine_getgameobject(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Engine.EngineEngineNode":
        line, expr_node = "self.engine", None

    elif expr_node.type_ == "Python.PythonAssignNode":
        line, expr_node = generate_python_assignment(expr_node, indent, generate_expression)
    elif expr_node.type_ == "Python.PythonPrintNode":
        line, expr_node = generate_python_print(expr_node, indent, generate_expression)
    elif expr_node.type_ == "Python.PythonAttributeNode":
        line, expr_node = generate_python_attribute(expr_node, indent, generate_expression)
    elif expr_node.type_ == "Python.PythonIdentifierNode":
        line, expr_node = expr_node.get_widget("Name").get_value(), None
    elif expr_node.type_ == "Python.PythonNumberNode":
        line, expr_node = expr_node.get_widget("Number").get_value(), None
    elif expr_node.type_ == "Python.PythonTextNode":
        line, expr_node = '"' + expr_node.get_widget("Text").get_value() + '"', None
    elif expr_node.type_ == "Python.PythonSelfNode":
        line, expr_node = "self", None
    elif expr_node.type_ == "Python.PythonNoneNode":
        line, expr_node = "None", None
    else:
        print(expr_node.type_)
        line, expr_node = "", None
    return line, expr_node
