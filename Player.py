from Entity import Entity


class Player(Entity):
    def __init__(self, player_name):
        super().__init__()
        self.player_name = player_name
 