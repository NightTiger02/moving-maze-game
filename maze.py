import pygame
import sys

import win32con
import win32gui

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
SCREEN_COLOR = (0, 0, 0)  # Black
SQUARE_SIZE = 20
SPEED = 5  # Adjust this value to control the movement speed
clock = pygame.time.Clock()

# Create the main screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse Follow")

# Initialize starting position
x, y = 50, 50
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_focused():
        # Get the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Check if the mouse is near the left edge
        if mouse_x < 10 and mouse_y < 10:
            x -= SPEED
        # Check if the mouse is near the right edge
        elif mouse_x > SCREEN_WIDTH - 10 and 10 < mouse_y < SCREEN_HEIGHT:
            x += SPEED
        # Check if the mouse is near the top edge
        if  mouse_x < SCREEN_WIDTH and mouse_y < 10:
            y -= SPEED
        # Check if the mouse is near the bottom edge
        elif mouse_x > (SCREEN_WIDTH - 10) and (SCREEN_HEIGHT - 10) < mouse_y < SCREEN_HEIGHT:
            y += SPEED
        hwnd = win32gui.FindWindow(None, "Mouse Follow")
        win32gui.SetWindowPos(hwnd, 0, x, y, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOZORDER)
        # Update the display
        screen.fill(SCREEN_COLOR)
    
        # Draw a small square at the mouse position
        pygame.draw.rect(screen, (255, 255, 255), (mouse_x - SQUARE_SIZE // 2, mouse_y - SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE))

    # Update the display
    pygame.display.flip()
    clock.tick(60)
# Quit Pygame
pygame.quit()
sys.exit()