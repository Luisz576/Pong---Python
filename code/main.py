# IMPORT
import pygame as game
import configs

from sys import exit
from player import Player
from ball import Ball

# INIT
game.init()

window = game.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
game.display.set_caption("Pong")

FONT = game.font.SysFont('arial', 30, True, False)

clock = game.time.Clock()
player1 = Player(window, configs.PLAYER_WIDTH * 3)
player2 = Player(window, configs.SCREEN_WIDTH - (configs.PLAYER_WIDTH * 4))
ball = Ball(window,
            (configs.SCREEN_WIDTH / 2 - configs.BALL_SIZE / 2, configs.SCREEN_HEIGHT / 2 - configs.BALL_SIZE / 2))

score_player1 = 0
score_player2 = 0


def point(player):
    global player1, player2, ball, score_player1, score_player2
    player1.reset()
    player2.reset()
    ball.reset()
    if player == 1:
        score_player1 += 1
    else:
        score_player2 += 1


# GAME LOOP
while True:
    # CLEAR SCREEN
    window.fill((0, 0, 0))
    # EVENTS
    for event in game.event.get():
        # EXIT
        if event.type == game.QUIT:
            game.quit()
            exit()
        # CONTROLLERS
        if event.type == game.KEYDOWN:
            if event.key in configs.PLAYER_1_CONTROLLS:
                player1.set_controller(event.key, False)
            if event.key in configs.PLAYER_2_CONTROLLS:
                player2.set_controller(event.key, False)
        if event.type == game.KEYUP:
            if event.key in configs.PLAYER_1_CONTROLLS:
                player1.set_controller(event.key, True)
            if event.key in configs.PLAYER_2_CONTROLLS:
                player2.set_controller(event.key, True)
    # UPDATE COMPONENTS
    player1.update()
    player2.update()
    ball.update(player1, player2)
    window.blit(FONT.render(f"{score_player1} | {score_player2}", True, configs.WHITE_COLOR),
                (configs.SCREEN_WIDTH / 2 - 20, 20))
    # POINT
    if ball.position[0] < 0:
        point(2)
    elif ball.position[0] > configs.SCREEN_WIDTH:
        point(1)
    # UPDATE SCREEN
    game.display.update()
    # DELAY
    clock.tick(configs.TICKS)
