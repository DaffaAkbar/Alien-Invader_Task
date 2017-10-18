class GameStats():
    def __init__(self, setting,screen,ship):
        self.setting = setting
        self.screen = screen
        self.ship = ship

        self.game_active = False
        self.high_score = 0
        self.screen_rect = self.screen.get_rect()
        self.reset_stats()

    def reset_stats(self):
        self.ship.rect.centerx = self.screen_rect.centerx
        self.ship_left = self.setting.ship_limit
        self.score = 0