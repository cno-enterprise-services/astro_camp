# Lesson 3: Adding Movement and Collision Detection
Welcome to Lesson 3 of creating your Mars Rover game! In this lesson, you'll learn how to make things move in the game environment using Pygame. By the end of this lesson, you'll have a complete game.

## Learning Objectives
By the end of this lesson, students will be able to:
1. Implement player movement using keyboard input
2. Apply boundary checks to keep objects within the game screen
3. Create and implement basic collision detection between game objects

<!-- ## Arkansas CS Standards Addressed
1. CSK8.G5.2.3: Compare and contrast the relative positions of objects using ordered pairs within a program
2. CSK8.G7.1.1: Identify and utilize level-appropriate, algorithmic problem-solving strategies
3. CSK8.G8.1.4: Apply strategies for identifying and solving routine hardware and software problems that occur in everyday computer use -->

## Step-by-Step Tutorial

### Step 1: Implementing Player Movement

We'll use event handling for keypress and keyup to control player movement:

```python
direction_y = 0
direction_x = 0

# Inside the game loop
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            direction_y = 1
        elif event.key == pygame.K_DOWN:
            direction_y = -1
        elif event.key == pygame.K_LEFT:
            direction_x = -1
        elif event.key == pygame.K_RIGHT:
            direction_x = 1
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            direction_y = 0
        elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            direction_x = 0

# Update player position
rover.y_pos -= direction_y * level_speed
rover.x_pos += direction_x * level_speed

# Keep player within screen bounds
rover.x_pos = max(0, min(rover.x_pos, SCREEN_WIDTH - rover.width))
rover.y_pos = max(0, min(rover.y_pos, SCREEN_HEIGHT - rover.height))
```

### Step 2: Collision Detection

We'll use the `detect_collision` method in our GameObject class:

```python
def detect_collision(self, other_body):
    if (self.x_pos < other_body.x_pos + other_body.width and
        self.x_pos + self.width > other_body.x_pos and
        self.y_pos < other_body.y_pos + other_body.height and
        self.y_pos + self.height > other_body.y_pos):
        return True
    return False
```

### Step 3: Implementing Game Logic

We'll use collision detection in the game loop:

```python
# Check for collisions
if rover.detect_collision(enemy_0):
    is_game_over = True
    did_win = False
    text = font.render('You Lose!', True, BLACK_COLOR)
    self.game_screen.blit(text, (275, 350))
elif rover.detect_collision(dest):
    is_game_over = True
    did_win = True
    text = font.render('You Win!', True, BLACK_COLOR)
    self.game_screen.blit(text, (275, 350))
```

## Challenges

1. Add acceleration and deceleration to the player's movement.
2. Create a moving enemy that bounces off the screen edges.
3. Implement a scoring system based on time or collected items.

## Reflection Questions

1. How does the collision detection algorithm work? Can you think of ways to optimize it?
2. What other types of movement could we implement for the player or enemies?
3. How might we use collision detection to create more complex game mechanics?
