from editor.nodes.nodes.testing_node import TestingNode
from editor.nodes.nodes.pe4_events_nodes import *
from editor.nodes.nodes.python_nodes import *
from editor.nodes.nodes.pe4_gameobject_nodes import *
from editor.nodes.nodes.pe4_engine_nodes import *

nodes = [
    TestingNode, InitNode, UpdateNode, AssignNode, LiteralNode, AttributeNode, GetComponentNode, PrintNode,
    IdentifierNode, AddChildNode, AddComponentNode, SelfNode, GameObjectNode, EngineNode, TakeScreenshotNode, NoneNode,
    GetGameSizeNode, StopGameNode, GetCurrentSceneNode, GetGameObjectNode
]
