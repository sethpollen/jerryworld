#!/usr/bin/env python3

import pygame
import sys

pygame.init()
pygame.display.set_caption("jerryworld")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
square_rect = pygame.Rect(10, 10, 50, 50)

# Game loop.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                break

    # Draw a red square on a black background.
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, square_rect)

    # Update the display.
    pygame.display.flip()

# Clean up and exit.
pygame.quit()
sys.exit()
