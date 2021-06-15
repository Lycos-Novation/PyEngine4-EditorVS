def generate_vec2_coords(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        vec = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        vec = ""

    line = indent * " " + vec + ".coords()"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_vec2_distance(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        vec = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        vec = ""
    if len(node.connected_input_nodes()[node.input(2)]):
        vec2 = generate_expression(node.connected_input_nodes()[node.input(2)][0])[0]
    else:
        vec2 = ""

    line = indent * " " + vec + ".distance("+vec2+")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_vec2_normalized(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        vec = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        vec = ""

    line = indent * " " + vec + ".normalized()"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_vec2_setcoords(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        vec = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        vec = ""
    if len(node.connected_input_nodes()[node.input(2)]):
        x = generate_expression(node.connected_input_nodes()[node.input(2)][0])[0]
    else:
        x = ""
    if len(node.connected_input_nodes()[node.input(3)]):
        y = generate_expression(node.connected_input_nodes()[node.input(3)][0])[0]
    else:
        y = ""

    line = indent * " " + vec + ".set_coords("+x+", "+y+")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_vec2_vec2(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        x = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        x = ""
    if len(node.connected_input_nodes()[node.input(2)]):
        y = generate_expression(node.connected_input_nodes()[node.input(2)][0])[0]
    else:
        y = ""

    line = indent * " " + "Vec2("+x+", "+y+")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_vec2_zero(node, indent, generate_expression):

    line = indent * " " + "Vec2.zero()"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_vec2_x(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(0)]):
        vec = generate_expression(node.connected_input_nodes()[node.input(0)][0])[0]
    else:
        vec = ""

    line = indent * " " + vec + ".x"
    return line, None


def generate_vec2_y(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(0)]):
        vec = generate_expression(node.connected_input_nodes()[node.input(0)][0])[0]
    else:
        vec = ""

    line = indent * " " + vec + ".y"
    return line, None
