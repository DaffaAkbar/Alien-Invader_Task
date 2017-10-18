class Setting():
    def __init__(self):
        #Screen Settings
        g=1000
        x=600
        self.width = g
        self.height = x
        self.color = (0,0,0)

        #Ship Settings
        self.ship_limit = 2

        #Bullet Settings
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 0,255,0
        self.bullets_allowed = 300
        self.enemy_bullets_allowed=300

        #Alien Settings
        self.drop_speed = 10

        #Game Speed Up
        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #INITIALIZE SETTING THAT CHANGE THROUGHOUT THE GAME.
        self.ship_speed = 1
        self.bullet_speed = 3
        self.alien_speed = 0.5
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)
        # print(self.alien_points)

