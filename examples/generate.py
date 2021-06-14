from files.scripts.script import Script
from files.utils.vec2 import Vec2


class Generate(Script):
    def __init__(self, engine):
        super().__init__(engine, "generate")

    def update(self, deltatime):
        print(self.game_object.get_component("TransformComponent").position.distance(Vec2.zero()))


