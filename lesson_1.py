import pygame

# Initialize Pygame
pygame.init()

# Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mars Rover Game")

# Load and scale background image
background = pygame.image.load('assets/Tharsis_Region.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Game loop
running = True
while running:

# Event handling
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

# Draw background
screen.blit(background, (0, 0))

# Update display
pygame.display.flip()

# Quit Pygame
pygame.quit()