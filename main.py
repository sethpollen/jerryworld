#!/usr/bin/env python3

import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("jerryworld")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
SQUARE_SIZE = 50

square_x = (SCREEN_WIDTH / 2) - (SQUARE_SIZE / 2)
square_y = (SCREEN_HEIGHT / 2) - (SQUARE_SIZE / 2)
square_rect = pygame.Rect(square_x, square_y, SQUARE_SIZE, SQUARE_SIZE)

# Game loop.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                break

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the red square (surface, color, rect object)
    pygame.draw.rect(screen, RED, square_rect)

    # 3. Update the display
    pygame.display.flip()

# Clean up and exit.
pygame.quit()
sys.exit()
