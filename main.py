import sys
from time import sleep

import pygame
vec2 = pygame.math.Vector2


pygame.init()

size = width, height = 640, 480
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("CurvedRaces")


points = [vec2(350, 250), vec2(0, 0), vec2(200, 200), vec2(300, 300)]
player_point = points[0]
speed = vec2(0, 0)


def transform(center, point):
    return point - center


def draw_point(surface, pos):
    pygame.draw.circle(surface, (255, 255, 255), pos, 8)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        speed[1] -= 0.1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        speed[1] += 0.1
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        speed[0] -= 0.1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        speed[0] += 0.1
    if keys[pygame.K_SPACE]:
        player_point = vec2(200, 200)
        points[0] = player_point

    speed *= 0.995
    player_point += speed

    screen.fill(black)
    for p in points:
        draw_point(screen, vec2(width / 2, height / 2) + transform(player_point, p))

    sleep(0.005)
    pygame.display.flip()
