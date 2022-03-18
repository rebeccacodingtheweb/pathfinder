DEFENCE = {
    "fortitude": {
        "name": "Fortitude",
        "stat": "con",
    },
    "reflex": {
        "name": "Reflex",
        "stat": "dex",
    },
    "will": {
        "name": "Will",
        "stat": "wis",
    },
}

PROFICIENCY_VALUES = {
    "Untrained": 0,
    "Trained": 2,
    "Expert": 4,
    "Master": 6,
    "Legendary": 8
}

class Defence:
    def __init__(self, type):
        self.type = DEFENCE[type]["name"]
        self.stat = DEFENCE[type]["stat"]
        self.proficiency = 'Untrained'
        self.proficiency_value = 0
        self.modifier = 0
        self.item_bonus = 0

    def change_modifier(self, stat, modifier):
        if self.stat == stat:
            self.modifier = modifier

    def change_proficiency(self, proficiency):
        self.proficiency = proficiency

    def change_proficiency_value(self, level):
        if self.proficiency != 'Untrained':
            self.proficiency_value = level + PROFICIENCY_VALUES[self.proficiency]

    def get_total(self):
        return self.proficiency_value + self.modifier + self.item_bonus

