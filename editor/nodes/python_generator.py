import os


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
        line, expr_node = generate_getcomponent(expr_node, indent)
    elif expr_node.type_ == "PE4.GameObject.AddChildNode":
        line, expr_node = generate_addchild(expr_node, indent)
    elif expr_node.type_ == "PE4.GameObject.AddComponentNode":
        line, expr_node = generate_addcomponent(expr_node, indent)

    elif expr_node.type_ == "Python.AssignNode":
        line, expr_node = generate_assignment(expr_node, indent)
    elif expr_node.type_ == "Python.PrintNode":
        line, expr_node = generate_print(expr_node, indent)
    elif expr_node.type_ == "Python.AttributeNode":
        line, expr_node = generate_attribute(expr_node, indent)

    elif expr_node.type_ == "PE4.GameObject.GameObjectNode":
        line, expr_node = "self.game_object", None
    elif expr_node.type_ == "PE4.Engine.EngineNode":
        line, expr_node = "self.engine", None
    elif expr_node.type_ == "Python.IdentifierNode":
        line, expr_node = expr_node.get_widget("Name").get_value(), None
    elif expr_node.type_ == "Python.LiteralNode":
        line, expr_node = '"' + expr_node.get_widget("Text").get_value() + '"', None
    elif expr_node.type_ == "Python.SelfNode":
        line, expr_node = "self", None
    elif expr_node.type_ == "Python.NoneNode":
        line, expr_node = "None", None
    else:
        print(expr_node.type_)
        line, expr_node = "", None
    return line, expr_node


def generate_attribute(attribute_node, indent):
    if len(attribute_node.connected_input_nodes()[attribute_node.input(0)]):
        object_ = generate_expression(attribute_node.connected_input_nodes()[attribute_node.input(0)][0])[0]
    else:
        object_ = ""

    if len(attribute_node.connected_input_nodes()[attribute_node.input(1)]):
        value = generate_expression(attribute_node.connected_input_nodes()[attribute_node.input(1)][0])[0]
    else:
        value = ""

    line = indent * " " + object_ + "." + value

    return line, None


def generate_print(print_node, indent):
    if len(print_node.connected_input_nodes()[print_node.input(1)]):
        value = generate_expression(print_node.connected_input_nodes()[print_node.input(1)][0])[0]
    else:
        value = None

    if value is not None:
        line = indent * " " + "print("+value+")"
    else:
        line = indent * " " + "print()"

    if len(print_node.connected_output_nodes()[print_node.output(0)]):
        return line, print_node.connected_output_nodes()[print_node.output(0)][0]
    return line, None


def generate_getcomponent(getcomp_node, indent):
    if len(getcomp_node.connected_input_nodes()[getcomp_node.input(1)]):
        gameobject = generate_expression(getcomp_node.connected_input_nodes()[getcomp_node.input(1)][0])[0]
    else:
        gameobject = ""

    if len(getcomp_node.connected_input_nodes()[getcomp_node.input(2)]):
        component = generate_expression(getcomp_node.connected_input_nodes()[getcomp_node.input(2)][0])[0]
    else:
        component = ""

    line = indent * " " + gameobject + ".get_component("+component+")"

    if len(getcomp_node.connected_output_nodes()[getcomp_node.output(0)]):
        return line, getcomp_node.connected_output_nodes()[getcomp_node.output(0)][0]
    return line, None


def generate_addcomponent(addcomp_node, indent):
    if len(addcomp_node.connected_input_nodes()[addcomp_node.input(1)]):
        gameobject = generate_expression(addcomp_node.connected_input_nodes()[addcomp_node.input(1)][0])[0]
    else:
        gameobject = ""

    if len(addcomp_node.connected_input_nodes()[addcomp_node.input(2)]):
        component = generate_expression(addcomp_node.connected_input_nodes()[addcomp_node.input(2)][0])[0]
    else:
        component = ""

    line = indent * " " + gameobject + ".add_component("+component+")"

    if len(addcomp_node.connected_output_nodes()[addcomp_node.output(0)]):
        return line, addcomp_node.connected_output_nodes()[addcomp_node.output(0)][0]
    return line, None


def generate_addchild(addchild_node, indent):
    if len(addchild_node.connected_input_nodes()[addchild_node.input(1)]):
        gameobject = generate_expression(addchild_node.connected_input_nodes()[addchild_node.input(1)][0])[0]
    else:
        gameobject = ""

    if len(addchild_node.connected_input_nodes()[addchild_node.input(2)]):
        component = generate_expression(addchild_node.connected_input_nodes()[addchild_node.input(2)][0])[0]
    else:
        component = ""

    line = indent * " " + gameobject + ".add_child("+component+")"

    if len(addchild_node.connected_output_nodes()[addchild_node.output(0)]):
        return line, addchild_node.connected_output_nodes()[addchild_node.output(0)][0]
    return line, None


def generate_assignment(assign_node, indent):
    if len(assign_node.connected_input_nodes()[assign_node.input(1)]):
        identifier = generate_expression(assign_node.connected_input_nodes()[assign_node.input(1)][0])[0]
    else:
        identifier = ""

    if len(assign_node.connected_input_nodes()[assign_node.input(2)]):
        value, _ = generate_expression(assign_node.connected_input_nodes()[assign_node.input(2)][0], 0)
    else:
        value = ""

    line = " " * indent + identifier + " = " + value

    if len(assign_node.connected_output_nodes()[assign_node.output(0)]):
        return line, assign_node.connected_output_nodes()[assign_node.output(0)][0]
    return line, None
