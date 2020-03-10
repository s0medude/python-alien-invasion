import json
import os

class GameStats:
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.set_high_score()
        
    def reset_stats(self):
        self.ship_left =  self.settings.ship_limit
        self.score = 0
        self.level = 1

    def set_high_score(self):
        filename = 'high_score.json'
        score = 0
        f = None        
        if not os.path.isfile(filename) or os.stat(filename).st_size == 0:
            f = open(filename, 'w')
            json.dump(score, f)
        elif not f:
            f = open(filename)
            score = json.load(f)
        f.close()
        return score
        
        
        
        