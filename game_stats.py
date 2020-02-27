class GameStats:
    def __init__(self, game):
        self.settings = game.settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        self.ship_left =  self.settings.ship_limit