import sys
from time import sleep

import pygame


pygame.init()

size = width, height = 640, 480
black = (0, 0, 0)

screen = pygame.display.set_mode(size)


points = [[350, 250], [0, 0], [200, 200], [300, 300]]
player_point = points[0]
speed = [0, 0]


def draw_point(surface, pos):
    pygame.draw.circle(surface, (255, 255, 255), pos, 8)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if pygame.key.get_pressed()[pygame.K_UP]:
        speed[1] -= 0.1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        speed[1] += 0.1
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        speed[0] -= 0.1
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        speed[0] += 0.1
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        player_point = [200, 200]

    speed[0] *= 0.995
    speed[1] *= 0.995
    player_point[0] += speed[0]
    player_point[1] += speed[1]

    screen.fill(black)
    for p in points:
        draw_point(screen, p)

    sleep(0.0051)
    pygame.display.flip()
