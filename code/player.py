import pygame.draw as draw
import configs


class Player:
    def __init__(self, window, fixed_x):
        self.window = window
        self.fixedX = fixed_x
        self.y = 0
        self.velocity = 0
        self.body = None
        self.reset()

    def reset(self):
        self.y = configs.SCREEN_HEIGHT / 2 - configs.PLAYER_HEIGHT / 2

    def set_controller(self, key, is_up):
        if key == configs.PLAYER_1_CONTROLLS[0] or key == configs.PLAYER_2_CONTROLLS[0]:
            self.velocity = 0 if is_up else -configs.PLAYER_SPEED
        if key == configs.PLAYER_1_CONTROLLS[1] or key == configs.PLAYER_2_CONTROLLS[1]:
            self.velocity = 0 if is_up else configs.PLAYER_SPEED

    def update(self):
        self.y += self.velocity
        self.body = draw.rect(self.window, configs.WHITE_COLOR,
                              (self.fixedX, self.y, configs.PLAYER_WIDTH, configs.PLAYER_HEIGHT))
