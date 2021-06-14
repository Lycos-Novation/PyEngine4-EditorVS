from editor.nodes.nodes.testing_node import TestingNode
from editor.nodes.nodes.pe4_events_nodes import *
from editor.nodes.nodes.python_nodes import *
from editor.nodes.nodes.pe4_gameobject_nodes import *
from editor.nodes.nodes.pe4_engine_nodes import *
from editor.nodes.nodes.pe4_scene_nodes import *
from editor.nodes.nodes.pe4_vec2_nodes import *

nodes = [
    TestingNode,

    EventsInitNode, EventsUpdateNode,

    PythonAssignNode, PythonTextNode, PythonAttributeNode, PythonPrintNode, PythonNumberNode, PythonIdentifierNode,
    PythonSelfNode, PythonNoneNode, PythonAddNode, PythonSubNode, PythonMulNode, PythonDivNode,

    GOGetComponentNode, GOAddChildNode, GOAddComponentNode, GOGameObjectNode,

    EngineEngineNode, EngineTakeScreenshotNode, EngineGetGameSizeNode, EngineStopGameNode, EngineGetCurrentSceneNode,
    EngineGetGameObjectNode,

    Vec2SetCoordsNode, Vec2DistanceNode, Vec2CoordsNode, Vec2NormalizedNode, Vec2ZeroNode, Vec2YNode, Vec2XNode,
    Vec2Node,

    SceneAddGameObjectNode, SceneAddGameObjectsNode, SceneGetGameObjectNode
]
