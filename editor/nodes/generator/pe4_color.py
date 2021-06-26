def generate_color_color(node, indent, generate_expression):
    line = indent * " " + "Color()"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_color_darker(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        color = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        color = ""
    if len(node.connected_input_nodes()[node.input(2)]):
        force = generate_expression(node.connected_input_nodes()[node.input(2)][0])[0]
    else:
        force = 1

    line = indent * " " + color + ".darker("+force+")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_color_lighter(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        color = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        color = ""
    if len(node.connected_input_nodes()[node.input(2)]):
        force = generate_expression(node.connected_input_nodes()[node.input(2)][0])[0]
    else:
        force = "1"

    line = indent * " " + color + ".lighter("+force+")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_color_from_color(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        color = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        color = ""

    line = indent * " " + "Color.from_color("+color+")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_color_from_html(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        html = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        html = ""

    line = indent * " " + "Color.from_html("+html+")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_color_from_name(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        name = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        name = ""

    line = indent * " " + "Color.from_name("+name+")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_color_from_rgb(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        r = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        r = ""
    if len(node.connected_input_nodes()[node.input(2)]):
        g = generate_expression(node.connected_input_nodes()[node.input(2)][0])[0]
    else:
        g = ""
    if len(node.connected_input_nodes()[node.input(3)]):
        b = generate_expression(node.connected_input_nodes()[node.input(3)][0])[0]
    else:
        b = ""

    line = indent * " " + "Color.from_rgb("+r+", "+g+", "+b+")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_color_from_rgba(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        r = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        r = ""
    if len(node.connected_input_nodes()[node.input(2)]):
        g = generate_expression(node.connected_input_nodes()[node.input(2)][0])[0]
    else:
        g = ""
    if len(node.connected_input_nodes()[node.input(3)]):
        b = generate_expression(node.connected_input_nodes()[node.input(3)][0])[0]
    else:
        b = ""
    if len(node.connected_input_nodes()[node.input(4)]):
        a = generate_expression(node.connected_input_nodes()[node.input(3)][0])[0]
    else:
        a = ""

    line = indent * " " + "Color.from_rgba("+r+", "+g+", "+b+", "+a+")"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_color_rgb(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        color = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        color = ""

    line = indent * " " + color + ".rgb()"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_color_rgba(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        color = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        color = ""

    line = indent * " " + color + ".rgba()"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None


def generate_color_html(node, indent, generate_expression):
    if len(node.connected_input_nodes()[node.input(1)]):
        color = generate_expression(node.connected_input_nodes()[node.input(1)][0])[0]
    else:
        color = ""

    line = indent * " " + color + ".html()"

    if len(node.connected_output_nodes()[node.output(0)]):
        return line, node.connected_output_nodes()[node.output(0)][0]
    return line, None
