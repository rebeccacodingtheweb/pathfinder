STATS = ["str", "dex", "con", "int", "wis", "cha"]


class Stat():
    def __init__(self, stat):
        self.name = stat
        self.value = 10
        self.modifier = 0

    def update(self, new_value):
        self.value = new_value
        self.modifier = (self.value - 10) // 2
