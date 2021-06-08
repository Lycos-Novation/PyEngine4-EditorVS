def generate_python_attribute(attribute_node, indent, generate_expression):
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


def generate_python_print(print_node, indent, generate_expression):
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


def generate_python_assignment(assign_node, indent, generate_expression):
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


def generate_python_add(add_node, indent, generate_expression):
    if len(add_node.connected_input_nodes()[add_node.input(1)]):
        left = generate_expression(add_node.connected_input_nodes()[add_node.input(1)][0])[0]
    else:
        left = ""

    if len(add_node.connected_input_nodes()[add_node.input(2)]):
        right = generate_expression(add_node.connected_input_nodes()[add_node.input(2)][0])[0]
    else:
        right = ""

    line = indent * " " + "(" + left + " + " + right + ")"

    if len(add_node.connected_output_nodes()[add_node.output(0)]):
        return line, add_node.connected_output_nodes()[add_node.output(0)][0]
    return line, None


def generate_python_sub(sub_node, indent, generate_expression):
    if len(sub_node.connected_input_nodes()[sub_node.input(1)]):
        left = generate_expression(sub_node.connected_input_nodes()[sub_node.input(1)][0])[0]
    else:
        left = ""

    if len(sub_node.connected_input_nodes()[sub_node.input(2)]):
        right = generate_expression(sub_node.connected_input_nodes()[sub_node.input(2)][0])[0]
    else:
        right = ""

    line = indent * " " + "(" + left + " - " + right + ")"

    if len(sub_node.connected_output_nodes()[sub_node.output(0)]):
        return line, sub_node.connected_output_nodes()[sub_node.output(0)][0]
    return line, None


def generate_python_mul(mul_node, indent, generate_expression):
    if len(mul_node.connected_input_nodes()[mul_node.input(1)]):
        left = generate_expression(mul_node.connected_input_nodes()[mul_node.input(1)][0])[0]
    else:
        left = ""

    if len(mul_node.connected_input_nodes()[mul_node.input(2)]):
        right = generate_expression(mul_node.connected_input_nodes()[mul_node.input(2)][0])[0]
    else:
        right = ""

    line = indent * " " + "(" + left + " * " + right + ")"

    if len(mul_node.connected_output_nodes()[mul_node.output(0)]):
        return line, mul_node.connected_output_nodes()[mul_node.output(0)][0]
    return line, None


def generate_python_div(div_node, indent, generate_expression):
    if len(div_node.connected_input_nodes()[div_node.input(1)]):
        left = generate_expression(div_node.connected_input_nodes()[div_node.input(1)][0])[0]
    else:
        left = ""

    if len(div_node.connected_input_nodes()[div_node.input(2)]):
        right = generate_expression(div_node.connected_input_nodes()[div_node.input(2)][0])[0]
    else:
        right = ""

    line = indent * " " + "(" + left + " / " + right + ")"

    if len(div_node.connected_output_nodes()[div_node.output(0)]):
        return line, div_node.connected_output_nodes()[div_node.output(0)][0]
    return line, None
