from files.scripts.script import Script
from files.utils.color import Color


class Generate(Script):
    def __init__(self, engine):
        super().__init__(engine, "generate")
        print(Color().rgb())
        print(Color.from_name("RED").lighter(1).html())

