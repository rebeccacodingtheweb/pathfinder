from Stat import Stat

SIZE = ["tiny", "small", "medium", "large", "huge", "gargantuan"]
ALIGNMENT = ["LG", "LN", "LE", "NG", "N", "NE", "CG", "CN", "CE"]


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
        self.force = Stat("str")
        self.dex = Stat("dex")
        self.con = Stat("con")
        self.intel = Stat("int")
        self.wis = Stat("wis")
        self.cha = Stat("cha")

    def set_ancestry(self, new_ancestry):
        self.ancestry = new_ancestry

    def set_size(self, new_size):
        if new_size in SIZE:
            self.size = new_size

    def set_level(self, new_level):
        if type(new_level) == int:
            self.level = new_level

    def set_alignment(self, new_alignment):
        if new_alignment in ALIGNMENT:
            self.alignment = new_alignment

    def set_max_hp(self, new_max_hp):
        if type(new_max_hp) == int:
            self.max_hp = new_max_hp

    def set_current_hp(self, new_hp):
        if type(new_hp) == int:
            self.current_hp = new_hp

    def set_temp_hp(self, new_hp):
        if type(new_hp) == int:
            self.temp_hp = new_hp






