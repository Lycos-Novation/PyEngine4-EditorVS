from files.scripts.script import Script
from files.utils.vec2 import Vec2
from files.utils.math import *


class Generate(Script):
    def __init__(self, engine):
        super().__init__(engine, "generate")

    def update(self, deltatime):
        print(clamp(-10, Vec2.zero().x))
        print(distance_between_rect(Vec2.zero(), Vec2.zero(), Vec2.zero(), Vec2.zero()))


