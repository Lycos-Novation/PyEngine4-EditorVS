from files.scripts.script import Script


class Generate(Script):
    def __init__(self, engine):
        super().__init__(engine, "generate")

    def update(self, deltatime):
        self.game_object.get_component("TransformComponent")
        position = self.game_object.get_component("TransformComponent")
        position = position.position
        print(position)


