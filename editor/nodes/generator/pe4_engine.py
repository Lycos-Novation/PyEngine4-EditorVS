def generate_takescreenshot(takescreenshot_node, indent, generate_expression):
    if len(takescreenshot_node.connected_input_nodes()[takescreenshot_node.input(1)]):
        engine = generate_expression(takescreenshot_node.connected_input_nodes()[takescreenshot_node.input(1)][0])[0]
    else:
        engine = ""

    if len(takescreenshot_node.connected_input_nodes()[takescreenshot_node.input(2)]):
        path = generate_expression(takescreenshot_node.connected_input_nodes()[takescreenshot_node.input(2)][0])[0]
    else:
        path = None

    if len(takescreenshot_node.connected_input_nodes()[takescreenshot_node.input(3)]):
        pos = generate_expression(takescreenshot_node.connected_input_nodes()[takescreenshot_node.input(3)][0])[0]
    else:
        pos = None

    if len(takescreenshot_node.connected_input_nodes()[takescreenshot_node.input(4)]):
        size = generate_expression(takescreenshot_node.connected_input_nodes()[takescreenshot_node.input(4)][0])[0]
    else:
        size = None

    if path is not None and pos is not None and size is not None:
        line = indent * " " + engine + ".take_screenshot("+path+", "+pos+", "+size+")"
    elif path is not None and pos is not None:
        line = indent * " " + engine + ".take_screenshot("+path+", "+pos+")"
    elif path is not None and size is not None:
        line = indent * " " + engine + ".take_screenshot("+path+", size="+size+")"
    elif size is not None and pos is not None:
        line = indent * " " + engine + ".take_screenshot(pos="+pos+", size="+size+")"
    elif path is not None:
        line = indent * " " + engine + ".take_screenshot("+path+")"
    elif size is not None:
        line = indent * " " + engine + ".take_screenshot(size="+size+")"
    elif pos is not None:
        line = indent * " " + engine + ".take_screenshot(pos="+pos+")"
    else:
        line = indent * " " + engine + ".take_screenshot()"

    if len(takescreenshot_node.connected_output_nodes()[takescreenshot_node.output(0)]):
        return line, takescreenshot_node.connected_output_nodes()[takescreenshot_node.output(0)][0]
    return line, None


def generate_getgamesize(getgamesize_node, indent, generate_expression):
    if len(getgamesize_node.connected_input_nodes()[getgamesize_node.input(1)]):
        engine = generate_expression(getgamesize_node.connected_input_nodes()[getgamesize_node.input(1)][0])[0]
    else:
        engine = ""

    line = " " * indent + engine + ".get_game_size()"

    if len(getgamesize_node.connected_output_nodes()[getgamesize_node.output(0)]):
        return line, getgamesize_node.connected_output_nodes()[getgamesize_node.output(0)][0]
    return line, None


def generate_stopgame(stopgame_node, indent, generate_expression):
    if len(stopgame_node.connected_input_nodes()[stopgame_node.input(1)]):
        engine = generate_expression(stopgame_node.connected_input_nodes()[stopgame_node.input(1)][0])[0]
    else:
        engine = ""

    line = " " * indent + engine + ".stop_game()"

    if len(stopgame_node.connected_output_nodes()[stopgame_node.output(0)]):
        return line, stopgame_node.connected_output_nodes()[stopgame_node.output(0)][0]
    return line, None


def generate_getcurrentscene(getcurrentscene_node, indent, generate_expression):
    if len(getcurrentscene_node.connected_input_nodes()[getcurrentscene_node.input(1)]):
        engine = generate_expression(getcurrentscene_node.connected_input_nodes()[getcurrentscene_node.input(1)][0])[0]
    else:
        engine = ""

    line = " " * indent + engine + ".get_current_scene()"

    if len(getcurrentscene_node.connected_output_nodes()[getcurrentscene_node.output(0)]):
        return line, getcurrentscene_node.connected_output_nodes()[getcurrentscene_node.output(0)][0]
    return line, None


def generate_getgameobject(getgameobject_node, indent, generate_expression):
    if len(getgameobject_node.connected_input_nodes()[getgameobject_node.input(1)]):
        engine = generate_expression(getgameobject_node.connected_input_nodes()[getgameobject_node.input(1)][0])[0]
    else:
        engine = ""

    if len(getgameobject_node.connected_input_nodes()[getgameobject_node.input(2)]):
        id = generate_expression(getgameobject_node.connected_input_nodes()[getgameobject_node.input(2)][0])[0]
    else:
        id = ""

    line = " " * indent + engine + ".get_game_object(" + id + ")"

    if len(getgameobject_node.connected_output_nodes()[getgameobject_node.output(0)]):
        return line, getgameobject_node.connected_output_nodes()[getgameobject_node.output(0)][0]
    return line, None
