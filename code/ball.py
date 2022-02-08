import pygame.draw as draw
import configs

from random import randint


class Ball:
    def __init__(self, window, start_position):
        self.window = window
        self.SPEED = 0
        self._start_position = start_position
        self.position = (0, 0)
        self.direction = (0, 0)
        self.body = None
        self.reset()

    def reset(self):
        self.SPEED = configs.BALL_SPEED
        self.position = (self._start_position[0], self._start_position[1])
        self.direction = (1 if randint(0, 1) == 1 else -1, 1 if randint(0, 1) == 1 else -1)

    def _calculate_direction(self, player1, player2):
        x = self.direction[0]
        y = self.direction[1]
        if self.position[1] <= configs.BALL_SIZE:
            y = 1
        if self.position[1] >= configs.SCREEN_HEIGHT - configs.BALL_SIZE:
            y = -1
        if player1.fixedX + configs.PLAYER_WIDTH >= self.position[0] >= player1.fixedX + configs.PLAYER_WIDTH / 2 and \
                self.position[1] + configs.BALL_SIZE >= player1.y and \
                self.position[1] <= player1.y + configs.PLAYER_HEIGHT:
            x = 1
        if self.position[0] + configs.BALL_SIZE >= player2.fixedX and \
                self.position[0] <= player2.fixedX + configs.PLAYER_WIDTH / 2 and \
                self.position[1] + configs.BALL_SIZE >= player2.y and \
                self.position[1] <= player2.y + configs.PLAYER_HEIGHT:
            x = -1
        return x, y

    def update(self, player1, player2):
        self.direction = self._calculate_direction(player1, player2)
        self.position = (self.position[0] + self.direction[0] * self.SPEED,
                         self.position[1] + self.direction[1] * self.SPEED)
        self.body = draw.rect(self.window, configs.WHITE_COLOR,
                              (self.position[0], self.position[1], configs.BALL_SIZE, configs.BALL_SIZE))
