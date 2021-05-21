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
                                        generate_function(init.connected_output_nodes()[init.output(0)][0]))
        else:
            template = template.replace("{INIT_BODY}", "")
    else:
        template = template.replace("{INIT_BODY}", "")

    update = graph.get_node_by_name("Update")
    if update is not None:
        if len(update.connected_output_nodes()[update.output(0)]):
            template = template.replace("{FUNCTIONS}", "    def update(self, deltatime):\n{FUNCTIONS}")
            template = template.replace("{FUNCTIONS}",
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
        line, function_node = generate_function(function_node, 8)
        lines.append(line)
    return "\n".join(lines)


def generate_function(function_node, indent=4):
    if function_node.type_ == "Python.AssignNode":
        line, function_node = generate_assignment(function_node, indent)
    elif function_node.type_ == "PE4.GetComponentNode":
        line, function_node = generate_getcomponent(function_node, indent)
    else:
        line, function_node = "", None
    return line, function_node


def generate_getcomponent(getcomp_node, indent):
    if len(getcomp_node.connected_input_nodes()[getcomp_node.input(1)]):
        component = generate_text(getcomp_node.connected_input_nodes()[getcomp_node.input(1)][0])
    else:
        component = ""

    line = indent * " " + "self.game_object.get_component("+component+")"

    if len(getcomp_node.connected_output_nodes()[getcomp_node.output(0)]):
        return line, getcomp_node.connected_output_nodes()[getcomp_node.output(0)][0]
    return line, None


def generate_assignment(assign_node, indent):
    if len(assign_node.connected_input_nodes()[assign_node.input(1)]):
        identifier = generate_text(assign_node.connected_input_nodes()[assign_node.input(1)][0])
    else:
        identifier = ""

    if len(assign_node.connected_input_nodes()[assign_node.input(2)]):
        value, _ = generate_function(assign_node.connected_input_nodes()[assign_node.input(2)][0], 0)
    else:
        value = ""

    line = " " * indent + identifier + " = " + value

    if len(assign_node.connected_output_nodes()[assign_node.output(0)]):
        return line, assign_node.connected_output_nodes()[assign_node.output(0)][0]
    return line, None


def generate_text(text_node):
    if text_node.type_ == "Python.IdentifierNode":
        return generate_identifier(text_node)
    elif text_node.type_ == "Python.LiteralNode":
        return generate_literal(text_node)
    else:
        return ""


def generate_identifier(identifier_node):
    return identifier_node.get_widget("Name").get_value()


def generate_literal(literal_node):
    return '"' + literal_node.get_widget("Text").get_value() + '"'

