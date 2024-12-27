# Lesson Plan 3: Adding Movement and Collision Detection

## Learning Objectives
- Implement player movement using keyboard input
- Understand and implement basic collision detection
- Create win and lose conditions for the game
  
## Computer Science and STEM Standards
### Arkansas CS Standards Addressed
1. CSK8.G5.2.3: Compare and contrast the relative positions of objects using ordered pairs within a program
2. CSK8.G7.1.1: Identify and utilize level-appropriate, algorithmic problem-solving strategies
3. CSK8.G8.1.4: Apply strategies for identifying and solving routine hardware and software problems that occur in everyday computer use

## Key Concepts
1. Handling keyboard input in Pygame
2. Updating object positions based on user input
3. Implementing boundary checks to keep objects on screen
4. Basic collision detection between game objects
5. Creating game states (win/lose conditions)

## Code Explanation

### Player Movement
- Use `pygame.key.get_pressed()` to detect held down keys
- Update player position based on arrow key inputs
- Implement boundary checks to keep player on screen

### Collision Detection
- Create a `detect_collision` method in the GameObject class
- Check for overlapping rectangles between objects

### Win/Lose Conditions
- Check for collisions between player and enemy (lose condition)
- Check for collisions between player and destination (win condition)

## Code Example
```python
import pygame

# Initialize pygame
pygame.init()

# Define constants
SCREEN_TITLE = 'My Game'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

class GameObject:
    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

    def detect_collision(self, other_body):
        if (self.x_pos < other_body.x_pos + other_body.width and
            self.x_pos + self.width > other_body.x_pos and
            self.y_pos < other_body.y_pos + other_body.height and
            self.y_pos + self.height > other_body.y_pos):
            return True
        return False

class Game:
    TICK_RATE = 60

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction_y = 0
        direction_x = 0

        player = GameObject('assets/mars_rover_sprite.png', 375, 500, 50, 50)
        enemy_0 = GameObject('assets/martian_sprite.png', 20, 400, 50, 50)
        dest = GameObject('Assets/space_suit_1.png', 375, 50, 50, 80)

        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)

        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
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

            # Game logic here
            player.y_pos -= direction_y * level_speed
            player.x_pos += direction_x * level_speed
            
            # Keep player within screen bounds
            player.x_pos = max(0, min(player.x_pos, SCREEN_WIDTH - player.width))
            player.y_pos = max(0, min(player.y_pos, SCREEN_HEIGHT - player.height))

            # Draw objects
            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image, (0, 0))
            player.draw(self.game_screen)
            enemy_0.draw(self.game_screen)
            dest.draw(self.game_screen)

            # Check for collisions
            if player.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('You Lose!', True, BLACK_COLOR)
                self.game_screen.blit(text, (275, 350))
            elif player.detect_collision(dest):
                is_game_over = True
                did_win = True
                text = font.render('You Win!', True, BLACK_COLOR)
                self.game_screen.blit(text, (275, 350))

            pygame.display.update()
            clock.tick(self.TICK_RATE)

        # Wait for a moment before restarting or quitting
        pygame.time.wait(2000)

        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return

# Main game loop
if __name__ == "__main__":
    new_game = Game('assets/tharsis_region.jpg', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
    new_game.run_game_loop(1)

pygame.quit()

```

## Challenges
1. Modify movement speed and experiment with different values
2. Add diagonal movement (combining up/down with left/right)
3. Implement "wrapping" movement (exiting one side of the screen enters the opposite side)
4. Create multiple enemies with collision detection

## Learning Outcomes
- Understand how to create responsive game controls
- Learn basic game physics and boundary management
- Implement fundamental game logic for win/lose scenarios

