from Entity import Entity
from Skill import SKILLS, Skill


class Monster(Entity):
    def __init__(self):
        super().__init__()
        self.skills = {}


    def set_skills(self, list_skills):
        for element in list_skills:
            if element in SKILLS:
                self.skills[element] = Skill(element, self.stats[SKILLS[element]["stat"]])



goblin = Monster()
goblin.name = "Goblin"
skills = ["acrobatics", "athletics"]
goblin.set_skills(skills)
print(goblin.skills["athletics"].stat.name)
