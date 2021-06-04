from files.scripts.script import Script


class Generate(Script):
    def __init__(self, engine):
        super().__init__(engine, "generate")

    def update(self, deltatime):
        self.engine.take_screenshot()
        self.engine.stop_game()


