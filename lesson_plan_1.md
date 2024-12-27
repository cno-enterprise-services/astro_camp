# Lesson Plan 1

## Learning Objectives
- Understand basic Pygame setup
- Create a game window
- Load and display a background image
- Implement a basic game loop
- Handle game exit

## Code Example
```python
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
```


## Key Learning Points
1. `pygame.init()` starts Pygame.
2. `pygame.display.set_mode()` creates the game window.
3. `pygame.image.load()` imports images.
4. `pygame.transform.scale()` resizes images.
5. The game loop handles events and updates the display.
6. `pygame.display.flip()` refreshes the screen.
7. `pygame.quit()` closes Pygame properly.

## Challenges for Students
1. Change the window size.
2. Try different background images.
3. Add a print statement in the event loop to log events.
4. Experiment with different display update methods.
