from Stat import STATS, Stat
from Skill import SKILLS, Skill


class Player():
    def __init__(self, player_name):
        self.player_name = player_name
        self.force = 10
        self.dex = Stat("dex")
        self.con = 10
        self.intel = 10
        self.wis = 10
        self.cha = 10
        self.stats = []
        self.acrobatics = Skill("acrobatics", self.dex)
        # for stat in STATS:
        #     self.stats.append(Stat(stat))
