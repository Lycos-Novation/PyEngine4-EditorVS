def generate_getcomponent(getcomp_node, indent, generate_expression):
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


def generate_addcomponent(addcomp_node, indent, generate_expression):
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


def generate_addchild(addchild_node, indent, generate_expression):
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
