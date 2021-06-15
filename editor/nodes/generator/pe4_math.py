def generate_math_clamp(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        value = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        value = ""
    if len(node.connected_input_nodes()[node.input(2)]):
        mini = generate_expression(node.connected_input_nodes()[node.input(2)][0])[0]
    else:
        mini = None
    if len(node.connected_input_nodes()[node.input(3)]):
        maxi = generate_expression(node.connected_input_nodes()[node.input(3)][0])[0]
    else:
        maxi = None

    if mini is None and maxi is None:
        line = indent * " " + "clamp(" + value + ")"
    elif mini is None:
        line = indent * " " + "clamp(" + value + ", maxi=" + maxi + ")"
    elif maxi is None:
        line = indent * " " + "clamp(" + value + ", " + mini + ")"
    else:
        line = indent * " " + "clamp(" + value + ", " + mini + ", " + maxi + ")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_math_distance(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        pos = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        pos = ""
    if len(node.connected_input_nodes()[node.input(2)]):
        size = generate_expression(node.connected_input_nodes()[node.input(2)][0])[0]
    else:
        size = ""
    if len(node.connected_input_nodes()[node.input(3)]):
        pos2 = generate_expression(node.connected_input_nodes()[node.input(3)][0])[0]
    else:
        pos2 = ""
    if len(node.connected_input_nodes()[node.input(4)]):
        size2 = generate_expression(node.connected_input_nodes()[node.input(4)][0])[0]
    else:
        size2 = ""

    line = indent * " " + "distance_between_rect(" + pos + ", " + size + ", " + pos2 + ", " + size2 + ")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None
