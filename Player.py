from Entity import Entity
from Skill import SKILLS, Skill


class Player(Entity):
    def __init__(self, player_name):
        super().__init__()
        self.player_name = player_name
        self.skills = {}
        self.init_skills()

    def init_skills(self):
        for element in SKILLS:
            self.skills[element] = Skill(element, self.stats[SKILLS[element]["stat"]])

math = Player("mathieu")
print(math.skills["athletics"])
