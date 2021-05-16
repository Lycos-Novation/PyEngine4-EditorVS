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
                                        generate_function(update.connected_output_nodes()[update.output(0)][0]) +
                                        "\n\n{FUNCTIONS}")
        else:
            template = template.replace("{FUNCTIONS}", "    def update(self, deltatime):\n        pass\n\n{FUNCTIONS}")

    template = template.replace("{FUNCTIONS}", "")

    with open(file, "w") as f:
        f.write(template)


def generate_function(function_node, indent=4):
    lines = []
    while function_node is not None:
        if function_node.type_ == "Python.AssignNode":
            line, function_node = generate_assignment(function_node, 8)
        else:
            line, function_node = "", None

        lines.append(line)
    return "\n".join(lines)


def generate_assignment(assign_node, indent):
    line = " " * indent + "a = b"
    if len(assign_node.connected_output_nodes()[assign_node.output(0)]):
        return line, assign_node.connected_output_nodes()[assign_node.output(0)][0]
    return line, None
