import ast


def parse(ast_module, graph):
    start_nodes = []
    for i in ast_module.body:
        if isinstance(i, ast.ClassDef):
            print(i.name)
            for y in i.body:
                if isinstance(y, ast.FunctionDef):
                    start_nodes.append(parse_function(y, graph))
            break
    graph.auto_layout_nodes(start_nodes=start_nodes)
    for i in start_nodes:
        i.set_pos(i.x_pos() - 250, i.y_pos() - 0)
    graph.fit_to_selection()


def parse_function(ast_function, graph):
    function_node = None

    if ast_function.name == "__init__":
        function_node = graph.create_node('Events.InitNode', name="Init")
    elif ast_function.name == "update":
        function_node = graph.create_node('Events.UpdateNode', name="Update")

    if function_node is not None:
        last_node = function_node
        for i in ast_function.body:
            if isinstance(i, ast.Assign):
                last_node = parse_assign(i, last_node, graph)
            elif isinstance(i, ast.Expr):
                last_node = parse_expr(i, last_node, graph)

    print(ast_function.name)
    return function_node


def parse_expr(ast_expr, last_node, graph):
    if isinstance(ast_expr.value, ast.Call):
        return parse_call(ast_expr.value, last_node, graph)


def parse_assign(ast_assign, last_node, graph):
    assign_note = graph.create_node("Python.AssignNode", name="Assign")
    if isinstance(ast_assign.targets[0], ast.Name):
        string_node = parse_literal(ast_assign.targets[0], graph)
        assign_note.set_input(1, string_node.output(0))
    elif isinstance(ast_assign.targets[0], ast.Attribute):
        attribute_node = parse_attribute(ast_assign.targets[0], graph)
        assign_note.set_input(1, attribute_node.output(0))
    if isinstance(ast_assign.value, ast.Call):
        call_node = parse_call(ast_assign.value, None, graph)
        assign_note.set_input(2, call_node.output(1))
    elif isinstance(ast_assign.value, (ast.Constant, ast.Name)):
        constant_node = parse_literal(ast_assign.value, graph)
        assign_note.set_input(2, constant_node.output(0))
    assign_note.set_input(0, last_node.output(0))
    return assign_note


def parse_call(ast_call, last_node, graph):
    function_node = None

    if isinstance(ast_call.func, ast.Name):
        if ast_call.func.id == "print":
            function_node = graph.create_node("Python.PrintNode", name="Print")
    elif isinstance(ast_call.func, ast.Attribute):
        if ast_call.func.attr == "get_component":
            function_node = graph.create_node("PE4.GetComponentNode", name="Get Component")

    if function_node is None:
        return

    for i in range(len(ast_call.args)):
        if isinstance(ast_call.args[i], (ast.Name, ast.Constant)):
            arg_node = parse_literal(ast_call.args[i], graph)
            function_node.set_input(i+1, arg_node.output(0))
    if last_node is not None:
        function_node.set_input(0, last_node.output(0))
    return function_node


def parse_attribute(ast_attribute, graph):
    attribute_node = graph.create_node("Python.AttributeNode", name="Attribute")
    if isinstance(ast_attribute.value, ast.Attribute):
        value_node = parse_attribute(ast_attribute.value, graph)
        attribute_node.set_input(0, value_node.output(0))
    elif isinstance(ast_attribute.value, ast.Name):
        string_node = parse_literal(ast_attribute.value, graph)
        attribute_node.set_input(0, string_node.output(0))
    string_node = parse_literal(ast_attribute.attr, graph)
    attribute_node.set_input(1, string_node.output(0))
    return attribute_node


def parse_literal(ast_literal, graph):
    if isinstance(ast_literal, ast.Name):
        string_node = graph.create_node("Python.IdentifierNode", name="Identifier")
        string_node.get_widget("Name").set_value(str(ast_literal.id))
    elif isinstance(ast_literal, str):
        string_node = graph.create_node("Python.LiteralNode", name="Text")
        string_node.get_widget("Text").set_value(str(ast_literal))
    elif isinstance(ast_literal, ast.Constant):
        string_node = graph.create_node("Python.LiteralNode", name="Constant : "+type(ast_literal.value).__name__)
        string_node.get_widget("Text").set_value(str(ast_literal.value))
    return string_node
