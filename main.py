import math as m
import sys
from time import sleep

import pygame
vec2 = pygame.math.Vector2

import position
Pos = position.Position


pygame.init()

size = width, height = 640, 480
black = (0, 0, 0)

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("CurvedRaces")


points = [Pos(350, 250), Pos(0, 0), Pos(200, 200), Pos(300, 300)]
player_point = points[0]
speed = Pos(0, 0, 0)
acceleration = 0.1


def transform(center, point):
    result = point - center
    return result


def draw_point(surface, pos):
    radius = 8
    pygame.draw.circle(surface, (255, 255, 255), (pos.x, pos.y), radius)
    pygame.draw.line(surface, (255, 0, 0), (pos.x, pos.y),
                     (pos.x + radius * m.sin(pos.phi), pos.y - radius * m.cos(pos.phi)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            width = event.w
            height = event.h

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        speed.x += acceleration * m.sin(points[0].phi)
        speed.y += acceleration * m.cos(points[0].phi)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        speed.x -= acceleration * m.sin(points[0].phi)
        speed.y -= acceleration * m.cos(points[0].phi)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        speed.phi += 0.001
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        speed.phi -= 0.001
    if keys[pygame.K_SPACE]:
        player_point = Pos(200, 200)
        points[0] = player_point

    speed *= 0.99
    points[0] += speed

    screen.fill(black)
    print(transform(points[0], points[0]).phi)
    for p in points:
        draw_point(screen, Pos(width / 2, height / 2, 0) + transform(points[0], p))

    sleep(0.005)
    pygame.display.flip()
