SIZE = ["tiny", "small", "medium", "large", "huge", "gargantuan"]
ALIGNMENT = ["LG","LN","LE","NG", "N", "NE", "CG", "CN", "CE"]

class Entity:
    def __init__(self):
        self.name = "Unknown"
        self.ancestry = None
        self.size = "medium"
        self.level = 1
        self.alignment = "N"
        self.max_hp = 0
        self.current_hp = 0
        self.temp_hp = 0




