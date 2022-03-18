SKILLS = {
    "acrobatics": {
        "name": "Acrobatics",
        "stat": "dex",
        "is_affected_armor": True
    },
    "arcana": {
        "name": "Arcana",
        "stat": "int",
        "is_affected_armor": False
    },
    "athletics": {
        "name": "Athletics",
        "stat": "str",
        "is_affected_armor": True
    },
    "crafting": {
        "name": "Crafting",
        "stat": "int",
        "is_affected_armor": False
    },
    "deception": {
        "name": "Decption",
        "stat": "cha",
        "is_affected_armor": False
    },
    "diplomacy": {
        "name": "Diplomacy",
        "stat": "cha",
        "is_affected_armor": False
    },
    "intimidation": {
        "name": "Intimidation",
        "stat": "cha",
        "is_affected_armor": False
    },
    "medicine": {
        "name": "Medicine",
        "stat": "int",
        "is_affected_armor": False
    },
    "nature": {
        "name": "Nature",
        "stat": "wis",
        "is_affected_armor": False
    },
    "occultism": {
        "name": "Occultism",
        "stat": "int",
        "is_affected_armor": False
    },
    "performance": {
        "name": "Performance",
        "stat": "cha",
        "is_affected_armor": False
    },
    "religion": {
        "name": "Religion",
        "stat": "wis",
        "is_affected_armor": False
    },
    "society": {
        "name": "Society",
        "stat": "int",
        "is_affected_armor": False
    },
    "stealth": {
        "name": "Stealth",
        "stat": "dex",
        "is_affected_armor": True
    },
    "survival": {
        "name": "Survival",
        "stat": "wis",
        "is_affected_armor": False
    },
    "thievery": {
        "name": "Thievery",
        "stat": "dex",
        "is_affected_armor": True
    },
}

PROFICIENCY_VALUES = {
    "Untrained": 0,
    "Trained": 2,
    "Expert": 4,
    "Master": 6,
    "Legendary": 8
}

class Skill:
    def __init__(self, type):
        self.type = SKILLS[type]["name"]
        self.stat = SKILLS[type]["stat"]
        self.proficiency = 'Untrained'
        self.proficiency_value = 0
        self.modifier = 0
        self.armor_pen = 0
        self.is_affected_armor = SKILLS[type]["is_affected_armor"]
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
        return self.proficiency_value + self.modifier + self.item_bonus - self.armor_pen

