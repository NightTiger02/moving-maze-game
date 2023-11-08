import pygame
import sys
from pygame.locals import *
import win32con
import win32gui

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
SCREEN_COLOR = (0, 0, 0)  # Black
SQUARE_SIZE = 20
SPEED = 2  # Adjust this value to control the movement speed
clock = pygame.time.Clock()

# Create the main screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse Follow")

# Initialize starting position
x, y = 250, 250
hwnd = win32gui.FindWindow(None, "Mouse Follow")
win32gui.SetWindowPos(hwnd, 0, x, y, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOZORDER)
# Set up maze and screen
screen.fill(SCREEN_COLOR)
mask_rect = pygame.Rect(x, y, SCREEN_WIDTH+x, SCREEN_HEIGHT+y)
large_screen = pygame.image.load('maze.png')
screen.blit(large_screen, (-x, -y), mask_rect)
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_x, mouse_y = pygame.mouse.get_pos()
    try:
        if pygame.mouse.get_focused() and (screen.get_at((mouse_x, mouse_y))[0] > 100):
            # Check if the mouse is near the left edge
            if mouse_x < 5 and mouse_y < SCREEN_HEIGHT: #pos = 0, 50
                x -= SPEED
            # Check if the mouse is near the right edge
            if mouse_x > (SCREEN_WIDTH - 5) and mouse_y < SCREEN_HEIGHT: #pos = 200, 50
                x += SPEED
            # Check if the mouse is near the top edge
            if mouse_x < SCREEN_WIDTH and mouse_y < 5: #pos = 50, 0
                y -= SPEED
            # Check if the mouse is near the bottom edge
            if mouse_x < SCREEN_WIDTH and (SCREEN_HEIGHT - 5) < mouse_y: #pos = 50, 200
                y += SPEED
            hwnd = win32gui.FindWindow(None, "Mouse Follow")
            win32gui.SetWindowPos(hwnd, 0, x, y, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOZORDER)

            # Update the display
            screen.fill(SCREEN_COLOR)
            mask_rect = pygame.Rect(x, y, SCREEN_WIDTH+x, SCREEN_HEIGHT+y)
            screen.blit(large_screen, (-x, -y), mask_rect)
    except:
        pass
    # Update the display
    pygame.display.flip()
    clock.tick(60)
# Quit Pygame
pygame.quit()
sys.exit()