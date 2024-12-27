# Lesson Plan 2: Creating Game Objects

## Learning Objectives
- Understand Object-Oriented Programming (OOP) basics
- Create a GameObject class
- Load and scale game sprites
- Position game objects on the screen

## Computer Science and STEM Standards
### Arkansas CS Standards Addressed
1. CSK8.G7.2.2: Utilize variables to construct expressions and equations
2. CSK8.G6.3.1: Represent a variety of data in multiple formats
3. CSK8.G8.2.2: Utilize variables in the creation of functions, methods, or similar constructs

## Key Concepts
1. Class definition in Python
2. Image loading with Pygame
3. Object instantiation
4. Method creation

## Code Explanation

### GameObject Class
- `__init__` method initializes object properties
- Takes image path, x/y coordinates, width, and height
- Loads and scales image
- Stores position information

### Methods
- `draw()` method renders object on screen
- Allows easy placement of game elements

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
background = pygame.image.load('assets/tharsis_region.jpg')
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
martian = GameObject('assets/martian_sprite.png', 20, 400, 50, 50)

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

```

## Challenges
1. Create additional game objects
2. Experiment with different image sizes
3. Try positioning objects in different screen locations
4. Add more methods to the GameObject class

## Learning Outcomes
- Understand how to create reusable game object classes
- Learn basic image manipulation in Pygame
- Practice object-oriented programming principles
