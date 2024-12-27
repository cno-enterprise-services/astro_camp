# Lesson 2: Creating Game Objects
Welcome to Lesson 2 of creating your Mars Rover game! In this lesson, you'll learn how to add things to the game environment using Pygame. By the end of this lesson, you'll have a picture with all the elements in your game.

## Learning Objectives
By the end of this lesson, students will be able to:
1. Create a GameObject class to represent game elements
2. Load and scale sprite images for game objects
3. Position game objects on the screen
4. Understand and apply object-oriented programming concepts in game development

<!-- ## Arkansas CS Standards Addressed
1. CSK8.G7.2.2: Utilize variables to construct expressions and equations
2. CSK8.G6.3.1: Represent a variety of data in multiple formats
3. CSK8.G8.2.2: Utilize variables in the creation of functions, methods, or similar constructs -->

## Step-by-Step Tutorial

### Step 1: Creating the GameObject Class

First, we'll create a GameObject class to represent our game objects:

```python
class GameObject:
    def __init__(self, image_path, x, y, width, height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x_pos = x
        self.y_pos = y
```

Explanation:
- We define an `__init__` method that takes the image path, position (x, y), and dimensions.
- We load the image using `pygame.image.load()` and scale it using `pygame.transform.scale()`.
- We store the position and dimensions as attributes of the object.

### Step 2: Adding a Draw Method

Let's add a method to draw our game object on the screen:

```python
class GameObject:
    # ... (previous code)

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos, self.y_pos))
```

Explanation:
- The `draw` method takes the screen as an argument.
- We use `screen.blit()` to draw the image at the object's position.

### Step 3: Creating Game Objects

Now, let's create our game objects in the main game code:

```python
# Create game objects
rover = GameObject('assets/mars_rover_sprite.png', 375, 500, 50, 50)
martian = GameObject('assets/martian.png', 20, 400, 50, 50)
destination = GameObject('assets/mamers_vallis.jpg', 375, 50, 50, 50)
```

Explanation:
- We create instances of GameObject for the player (rover), enemy (martian), and destination.
- Each object is given an image path, initial position, and size.

### Step 4: Drawing Game Objects

In our game loop, we'll draw these objects:

```python
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background, (0, 0))
    
    # Draw game objects
    rover.draw(screen)
    martian.draw(screen)
    destination.draw(screen)
    
    # Update display
    pygame.display.flip()
```

Explanation:
- We call the `draw` method for each game object, passing the screen as an argument.
- This draws each object at its current position.

## Challenges

1. Add a new attribute to the GameObject class (e.g., `speed`) and use it to move the enemy.
2. Create multiple enemies at different positions on the screen.
3. Implement a method in the GameObject class to change the object's position.

## Reflection Questions

1. How does using a class for game objects make our code more organized?
2. Can you think of other attributes or methods that might be useful for our game objects?
3. How might we use this GameObject class to create different types of game elements (e.g., obstacles, power-ups)?

By completing this lesson, students will have created reusable game objects, applied object-oriented programming concepts, and laid the foundation for more complex game mechanics in future lessons.