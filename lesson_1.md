
# Lesson 1: Setting Up the Game Environment

Welcome to Lesson 1 of creating your Mars Rover game! In this lesson, you'll learn how to set up the basic game environment using Pygame. By the end of this lesson, you'll have a game window displaying a background image and a functional game loop.

---

## Learning Objectives
- Install and initialize Pygame
- Create a game window with specific dimensions
- Load and display a background image
- Implement a basic game loop
- Handle the quit event to close the game properly
  
---

## Step 1: Install Pygame

Before we begin, ensure you have Pygame installed. Open your terminal or command prompt and run:

```
pip install pygame
```

If you already have Pygame installed, you're good to go!

---

## Step 2: Import Pygame and Initialize It

The first step in any Pygame project is to import the library and initialize it. This sets up everything Pygame needs to function.

```
import pygame

# Initialize Pygame
pygame.init()
```

---

## Step 3: Create the Game Window

Next, we'll create a window for our game. We'll set its dimensions and give it a title.

```
# Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mars Rover Game")
```

This creates an 800x600 pixel window with the title "Mars Rover Game."

---

## Step 4: Load and Display a Background Image

Let's load an image to use as our game's background. Make sure you have an image file (e.g., `tharsis_tegion.jpg`) in an `assets` folder in the same directory as your script.

```
# Load and scale background image
background = pygame.image.load('assets/tharsis_region.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
```

This code loads the image and scales it to fit the screen dimensions.

---

## Step 5: Create the Game Loop

A game loop is essential for any game. It keeps the game running until the player decides to quit. Here's how we implement it:

```
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

### Explanation:
1. **Event Handling**: The `for event in pygame.event.get()` loop checks for events like closing the window.
2. **Drawing**: The `screen.blit()` function draws the background image onto the screen.
3. **Updating**: The `pygame.display.flip()` function refreshes the screen to show any changes.
4. **Quit**: When the player closes the window, `pygame.quit()` ensures Pygame shuts down properly.

---

## Complete Code

Here's what your complete code should look like:

```
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
background = pygame.image.load('assets/tharsis_tegion.jpg')
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

---

## Challenges

### Challenge 1: Change Window Size  
Modify `SCREEN_WIDTH` and `SCREEN_HEIGHT` to create a larger or smaller game window. Experiment with different dimensions.

### Challenge 2: Try Different Background Images  
Replace `tharsis_region.jpg` with another image file of your choice. Make sure it's located in the `assets` folder.

### Challenge 3: Add a Print Statement  
Inside the event loop (`for event in pygame.event.get()`), add a print statement to log events like mouse clicks or key presses. For example:
```
print(event)
```

### Challenge 4: Experiment with Display Updates  
Replace `pygame.display.flip()` with `pygame.display.update()`. Research how they differ and see if it affects your game's performance.

---

## Summary of Lesson 1

In this lesson, you:
1. Installed and initialized Pygame.
2. Created a game window with specific dimensions.
3. Loaded and displayed a background image.
4. Implemented a basic game loop.
5. Handled events like quitting the game.

You now have a functional starting point for your Mars Rover game! In **Lesson 2**, you'll learn how to create reusable game objects like your rover and martian.
