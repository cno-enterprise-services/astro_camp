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

# GameObject class
class GameObject:
    def __init__(self, image_path, x, y, width, height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x_pos = x
        self.y_pos = y

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos, self.y_pos))

# Create game objects
rover = GameObject('assets/mars_rover_sprite.png', 375, 500, 50, 50)
martian = GameObject('assets/martian.png', 20, 400, 50, 50)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background, (0, 0))
    
    # Draw game objects
    rover.draw(screen)
    martian.draw(screen)
    
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
