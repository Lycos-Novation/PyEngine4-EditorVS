import os

from editor.nodes.generator.python import *
from editor.nodes.generator.pe4_gameobject import *
from editor.nodes.generator.pe4_engine import *
from editor.nodes.generator.pe4_scene import *
from editor.nodes.generator.pe4_vec2 import *
from editor.nodes.generator.pe4_math import *
from editor.nodes.generator.pe4_color import *

imports = []


def generate(file, graph):
    global imports

    with open(os.path.join("editor", "res", "template.txt"), "r") as f:
        template = f.read()
    imports = []

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

    start = graph.get_node_by_name("Start")
    if start is not None:
        if len(start.connected_output_nodes()[start.output(0)]):
            template = template.replace("{FUNCTIONS}", "    def start(self):\n" +
                                        generate_functions(start.connected_output_nodes()[start.output(0)][0]) +
                                        "\n\n{FUNCTIONS}")
        else:
            template = template.replace("{FUNCTIONS}", "    def start(self):\n        pass\n\n{FUNCTIONS}")

    show = graph.get_node_by_name("Show")
    if show is not None:
        if len(show.connected_output_nodes()[show.output(0)]):
            template = template.replace("{FUNCTIONS}", "    def show(self, screen, camera_pos):\n" +
                                        generate_functions(show.connected_output_nodes()[show.output(0)][0]) +
                                        "\n\n{FUNCTIONS}")
        else:
            template = template.replace("{FUNCTIONS}",
                                        "    def show(self, screen, camera_pos):\n        pass\n\n{FUNCTIONS}")

    for i in ("Key Press", "Key Release", "Mouse Press", "Mouse Release", "Mouse Motion", "Mouse Wheel"):
        temp = graph.get_node_by_name(i)
        if temp is not None:
            if len(temp.connected_output_nodes()[temp.output(0)]):
                template = template.replace("{FUNCTIONS}", "    def "+i.replace(" ", "_").lower()+"(self, evt):\n" +
                                            generate_functions(temp.connected_output_nodes()[temp.output(0)][0]) +
                                            "\n\n{FUNCTIONS}")
            else:
                template = template.replace("{FUNCTIONS}", "    def "+i.replace(" ", "_").lower() +
                                            "(self, evt):\n        pass\n\n{FUNCTIONS}")

    template = template.replace("{FUNCTIONS}", "")
    if len(imports):
        template = template.replace("{IMPORTS}", "\n".join(imports))
    else:
        template = template.replace("{IMPORTS}\n", "")

    with open(file, "w") as f:
        f.write(template)


def generate_functions(function_node, indent=4):
    lines = []
    while function_node is not None:
        line, function_node = generate_expression(function_node, 8)
        lines.append(line)
    return "\n".join(lines)


def generate_expression(expr_node, indent=0):
    global imports

    if expr_node.type_ == "PE4.GameObject.GOGetComponentNode":
        line, expr_node = generate_go_getcomponent(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.GameObject.GOAddChildNode":
        line, expr_node = generate_go_addchild(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.GameObject.GOAddComponentNode":
        line, expr_node = generate_go_addcomponent(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.GameObject.GOGameObjectNode":
        line, expr_node = "self.game_object", None

    elif expr_node.type_ == "PE4.Math.MathClampNode":
        line, expr_node = generate_math_clamp(expr_node, indent, generate_expression)
        if "from files.utils.math import *" not in imports:
            imports.append("from files.utils.math import *")
    elif expr_node.type_ == "PE4.Math.MathDistanceBetweenRectNode":
        line, expr_node = generate_math_distance(expr_node, indent, generate_expression)
        if "from files.utils.math import *" not in imports:
            imports.append("from files.utils.math import *")

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

    elif expr_node.type_ == "PE4.Vec2.Vec2CoordsNode":
        line, expr_node = generate_vec2_coords(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Vec2.Vec2DistanceNode":
        line, expr_node = generate_vec2_distance(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Vec2.Vec2NormalizedNode":
        line, expr_node = generate_vec2_normalized(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Vec2.Vec2SetCoordsNode":
        line, expr_node = generate_vec2_setcoords(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Vec2.Vec2Node":
        line, expr_node = generate_vec2_vec2(expr_node, indent, generate_expression)
        if "from files.utils.vec2 import Vec2" not in imports:
            imports.append("from files.utils.vec2 import Vec2")
    elif expr_node.type_ == "PE4.Vec2.Vec2ZeroNode":
        line, expr_node = generate_vec2_zero(expr_node, indent, generate_expression)
        if "from files.utils.vec2 import Vec2" not in imports:
            imports.append("from files.utils.vec2 import Vec2")
    elif expr_node.type_ == "PE4.Vec2.Vec2XNode":
        line, expr_node = generate_vec2_x(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Vec2.Vec2YNode":
        line, expr_node = generate_vec2_y(expr_node, indent, generate_expression)

    elif expr_node.type_ == "PE4.Color.ColorHTMLNode":
        line, expr_node = generate_color_html(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Color.ColorRGBNode":
        line, expr_node = generate_color_rgb(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Color.ColorRGBANode":
        line, expr_node = generate_color_rgba(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Color.ColorLighterNode":
        line, expr_node = generate_color_lighter(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Color.ColorDarkerNode":
        line, expr_node = generate_color_darker(expr_node, indent, generate_expression)
    elif expr_node.type_ == "PE4.Color.ColorNode":
        line, expr_node = generate_color_color(expr_node, indent, generate_expression)
        if "from files.utils.color import Color" not in imports:
            imports.append("from files.utils.color import Color")
    elif expr_node.type_ == "PE4.Color.ColorFromColorNode":
        line, expr_node = generate_color_from_color(expr_node, indent, generate_expression)
        if "from files.utils.color import Color" not in imports:
            imports.append("from files.utils.color import Color")
    elif expr_node.type_ == "PE4.Color.ColorFromHTMLNode":
        line, expr_node = generate_color_from_html(expr_node, indent, generate_expression)
        if "from files.utils.color import Color" not in imports:
            imports.append("from files.utils.color import Color")
    elif expr_node.type_ == "PE4.Color.ColorFromRGBNode":
        line, expr_node = generate_color_from_rgb(expr_node, indent, generate_expression)
        if "from files.utils.color import Color" not in imports:
            imports.append("from files.utils.color import Color")
    elif expr_node.type_ == "PE4.Color.ColorFromRGBANode":
        line, expr_node = generate_color_from_rgba(expr_node, indent, generate_expression)
        if "from files.utils.color import Color" not in imports:
            imports.append("from files.utils.color import Color")
    elif expr_node.type_ == "PE4.Color.ColorFromNameNode":
        line, expr_node = generate_color_from_name(expr_node, indent, generate_expression)
        if "from files.utils.color import Color" not in imports:
            imports.append("from files.utils.color import Color")

    elif expr_node.type_ == "Python.PythonAssignNode":
        line, expr_node = generate_python_assignment(expr_node, indent, generate_expression)
    elif expr_node.type_ == "Python.PythonPrintNode":
        line, expr_node = generate_python_print(expr_node, indent, generate_expression)
    elif expr_node.type_ == "Python.PythonAttributeNode":
        line, expr_node = generate_python_attribute(expr_node, indent, generate_expression)
    elif expr_node.type_ == "Python.PythonAddNode":
        line, expr_node = generate_python_add(expr_node, indent, generate_expression)
    elif expr_node.type_ == "Python.PythonSubNode":
        line, expr_node = generate_python_sub(expr_node, indent, generate_expression)
    elif expr_node.type_ == "Python.PythonMulNode":
        line, expr_node = generate_python_mul(expr_node, indent, generate_expression)
    elif expr_node.type_ == "Python.PythonDivNode":
        line, expr_node = generate_python_div(expr_node, indent, generate_expression)
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
