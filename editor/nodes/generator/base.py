import os

from editor.nodes.generator.python import *
from editor.nodes.generator.pe4_gameobject import *
from editor.nodes.generator.pe4_engine import *


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
    if expr_node.type_ == "PE4.GameObject.GetComponentNode":
        line, expr_node = generate_getcomponent(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.GameObject.AddChildNode":
        line, expr_node = generate_addchild(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.GameObject.AddComponentNode":
        line, expr_node = generate_addcomponent(expr_node, indent, generate_expression)

    elif expr_node.type_ == "PE4.Engine.TakeScreenshotNode":
        line, expr_node = generate_takescreenshot(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Engine.GetGameSizeNode":
        line, expr_node = generate_getgamesize(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Engine.StopGameNode":
        line, expr_node = generate_stopgame(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Engine.GetCurrentSceneNode":
        line, expr_node = generate_getcurrentscene(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Engine.GetGameObjectNode":
        line, expr_node = generate_getgameobject(expr_node, indent, generate_expression)

    elif expr_node.type_ == "Python.AssignNode":
        line, expr_node = generate_assignment(expr_node, indent, generate_expression)
    elif expr_node.type_ == "Python.PrintNode":
        line, expr_node = generate_print(expr_node, indent, generate_expression)
    elif expr_node.type_ == "Python.AttributeNode":
        line, expr_node = generate_attribute(expr_node, indent, generate_expression)

    elif expr_node.type_ == "PE4.GameObject.GameObjectNode":
        line, expr_node = "self.game_object", None
    elif expr_node.type_ == "PE4.Engine.EngineNode":
        line, expr_node = "self.engine", None
    elif expr_node.type_ == "Python.IdentifierNode":
        line, expr_node = expr_node.get_widget("Name").get_value(), None
    elif expr_node.type_ == "Python.NumberNode":
        line, expr_node = expr_node.get_widget("Number").get_value(), None
    elif expr_node.type_ == "Python.TextNode":
        line, expr_node = '"' + expr_node.get_widget("Text").get_value() + '"', None
    elif expr_node.type_ == "Python.SelfNode":
        line, expr_node = "self", None
    elif expr_node.type_ == "Python.NoneNode":
        line, expr_node = "None", None
    else:
        print(expr_node.type_)
        line, expr_node = "", None
    return line, expr_node
