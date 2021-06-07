def generate_add_gameobject(addgameobject_node, indent, generate_expression):
    if len(addgameobject_node.connected_input_nodes()[addgameobject_node.input(1)]):
        scene = generate_expression(addgameobject_node.connected_input_nodes()[addgameobject_node.input(1)][0])[0]
    else:
        scene = ""

    if len(addgameobject_node.connected_input_nodes()[addgameobject_node.input(2)]):
        gameobject = generate_expression(addgameobject_node.connected_input_nodes()[addgameobject_node.input(2)][0])[0]
    else:
        gameobject = ""

    line = indent * " " + scene + ".add_game_object("+gameobject+")"

    if len(addgameobject_node.connected_output_nodes()[addgameobject_node.output(0)]):
        return line, addgameobject_node.connected_output_nodes()[addgameobject_node.output(0)][0]
    return line, None


def generate_add_gameobjects(addgameobjects_node, indent, generate_expression):
    if len(addgameobjects_node.connected_input_nodes()[addgameobjects_node.input(1)]):
        scene = generate_expression(addgameobjects_node.connected_input_nodes()[addgameobjects_node.input(1)][0])[0]
    else:
        scene = ""

    if len(addgameobjects_node.connected_input_nodes()[addgameobjects_node.input(2)]):
        gameobject = generate_expression(addgameobjects_node.connected_input_nodes()[addgameobjects_node.input(2)][0])[0]
    else:
        gameobject = ""

    line = indent * " " + scene + ".add_game_objects("+gameobject+")"

    if len(addgameobjects_node.connected_output_nodes()[addgameobjects_node.output(0)]):
        return line, addgameobjects_node.connected_output_nodes()[addgameobjects_node.output(0)][0]
    return line, None


def generate_get_gameobject(getgameobject_node, indent, generate_expression):
    if len(getgameobject_node.connected_input_nodes()[getgameobject_node.input(1)]):
        scene = generate_expression(getgameobject_node.connected_input_nodes()[getgameobject_node.input(1)][0])[0]
    else:
        scene = ""

    if len(getgameobject_node.connected_input_nodes()[getgameobject_node.input(2)]):
        id_ = generate_expression(getgameobject_node.connected_input_nodes()[getgameobject_node.input(2)][0])[0]
    else:
        id_ = ""

    line = indent * " " + scene + ".get_game_object("+id_+")"

    if len(getgameobject_node.connected_output_nodes()[getgameobject_node.output(0)]):
        return line, getgameobject_node.connected_output_nodes()[getgameobject_node.output(0)][0]
    return line, None
