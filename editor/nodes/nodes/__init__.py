from editor.nodes.nodes.testing_node import TestingNode
from editor.nodes.nodes.pe4_events_nodes import *
from editor.nodes.nodes.python_nodes import *
from editor.nodes.nodes.pe4_gameobject_nodes import *
from editor.nodes.nodes.pe4_engine_nodes import *
from editor.nodes.nodes.pe4_scene_nodes import *

nodes = [
    TestingNode,

    EventsInitNode, EventsUpdateNode,

    PythonAssignNode, PythonTextNode, PythonAttributeNode, PythonPrintNode, PythonNumberNode, PythonIdentifierNode,
    PythonSelfNode, PythonNoneNode,

    GOGetComponentNode, GOAddChildNode, GOAddComponentNode, GOGameObjectNode,

    EngineEngineNode, EngineTakeScreenshotNode, EngineGetGameSizeNode, EngineStopGameNode, EngineGetCurrentSceneNode,
    EngineGetGameObjectNode,

    SceneAddGameObjectNode, SceneAddGameObjectsNode, SceneGetGameObjectNode
]
