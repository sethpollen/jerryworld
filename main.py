#!/usr/bin/env python3

import pygame

# Set up pygame.
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 60

# Time (in seconds) which elapsed since the last frame.
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Draws the game screen.
def draw():
    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)

# Updates object positions and states.
def move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

while True:
    # Check for a quit signal from the user.
    if any([event.type == pygame.QUIT for event in pygame.event.get()]):
        break

    draw()
    move()

    pygame.display.flip()
    dt = clock.tick(FPS) / 1000

pygame.quit()
