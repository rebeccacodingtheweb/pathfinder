PROFICIENCY_VALUES = {
    "Untrained": 0,
    "Trained": 2,
    "Expert": 4,
    "Master": 6,
    "Legendary": 8
}
ARMOR_TYPES = {
    "Unarmored": "Untrained",
    "Light": "Untrained",
    "Medium": "Untrained",
    "Heavy": "Untrained"
}

class Ac:
    def __init__(self):
        self.armor_type = "Unarmored"
        self.dex_modifier = 0
        self.proficiency_type = "Untrained"
        self.proficiency_value = 0
        self.item_bonus = 0

    def change_proficiency(self, proficiency):
        self.proficiency = proficiency

    def change_proficiency_value(self, level):
        if self.proficiency != 'Untrained':
            self.proficiency_value = level + PROFICIENCY_VALUES[self.proficiency]

