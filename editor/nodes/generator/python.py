def generate_attribute(attribute_node, indent, generate_expression):
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


def generate_print(print_node, indent, generate_expression):
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


def generate_assignment(assign_node, indent, generate_expression):
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
