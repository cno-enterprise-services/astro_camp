# Lesson Plan 4: Advanced Features - Disappearing Martian and Play Again Menu

## Learning Objectives
- Implement a disappearing and reappearing game object
- Create a simple play again menu
- Understand game state management
- Learn to use Pygame's time module

## Computer Science and STEM Standards
### Arkansas CS Standards Addressed
1. CSK8.G7.3.5: Collect and analyze data from multiple sources
2. CSK8.G8.1.3: Demonstrate appropriate collaborative behaviors to solve problems
3. CSK8.G6.1.2: Utilize visual representations of problem-solving logic to solve problems of level-appropriate complexity

## Key Concepts
1. Using Pygame's time module for game events
2. Implementing periodic events in the game loop
3. Creating simple GUI elements for a menu
4. Managing game states (play, game over, restart)
5. Resetting game objects for a new game

## Code Explanation

### Disappearing Martian
- Use `pygame.time.get_ticks()` to track time
- Implement a timer for the martian's visibility changes
- Randomly reposition the martian when it reappears

### Play Again Menu
- Create a simple text-based menu using Pygame's font rendering
- Handle user input for menu choices
- Implement game reset functionality

## Code Example
```python
import pygame
import math
import random

# Initialize pygame
pygame.init()

# Define constants
SCREEN_TITLE = 'Mars Rover Game'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

class GameObject:
    def __init__(self, image_path, x, y, width, height):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height
        self.angle = 0

    def draw(self, background):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x_pos, self.y_pos)).center)
        background.blit(rotated_image, new_rect.topleft)

    def detect_collision(self, other_body):
        if (self.x_pos < other_body.x_pos + other_body.width and
            self.x_pos + self.width > other_body.x_pos and
            self.y_pos < other_body.y_pos + other_body.height and
            self.y_pos + self.height > other_body.y_pos):
            return True
        return False

class Game:
    TICK_RATE = 60
    MARTIAN_CHANGE_INTERVAL = 6000  # 90 seconds in milliseconds

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))
        self.font = pygame.font.Font(None, 36)

    def draw_popup(self, message):
        popup_width, popup_height = 300, 150
        popup_x = (SCREEN_WIDTH - popup_width) // 2
        popup_y = (SCREEN_HEIGHT - popup_height) // 2
        
        pygame.draw.rect(self.game_screen, WHITE_COLOR, (popup_x, popup_y, popup_width, popup_height))
        pygame.draw.rect(self.game_screen, BLACK_COLOR, (popup_x, popup_y, popup_width, popup_height), 2)
        
        text = self.font.render(message, True, BLACK_COLOR)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        self.game_screen.blit(text, text_rect)
        
        yes_text = self.font.render("Yes", True, BLACK_COLOR)
        no_text = self.font.render("No", True, BLACK_COLOR)
        yes_rect = yes_text.get_rect(center=(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 40))
        no_rect = no_text.get_rect(center=(SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 + 40))
        self.game_screen.blit(yes_text, yes_rect)
        self.game_screen.blit(no_text, no_rect)
        
        pygame.display.update()
        
        return yes_rect, no_rect

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        rotation_speed = 2
        movement_speed = level_speed

        player = GameObject('assets/mars_rover_sprite.png', 375, 500, 50, 50)
        enemy_0 = GameObject('assets/martian_sprite.png', 20, 400, 50, 50)
        dest = GameObject('assets/space_suit_1.png', 375, 50, 50, 80)

        clock = pygame.time.Clock()

        last_martian_change = pygame.time.get_ticks()

        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False  # Signal to completely exit the game

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.angle += rotation_speed
            if keys[pygame.K_RIGHT]:
                player.angle -= rotation_speed
            if keys[pygame.K_UP]:
                player.x_pos += movement_speed * math.cos(math.radians(player.angle))
                player.y_pos -= movement_speed * math.sin(math.radians(player.angle))
            if keys[pygame.K_DOWN]:
                player.x_pos -= movement_speed * math.cos(math.radians(player.angle))
                player.y_pos += movement_speed * math.sin(math.radians(player.angle))

            # Keep player within screen bounds
            player.x_pos = max(0, min(player.x_pos, SCREEN_WIDTH - player.width))
            player.y_pos = max(0, min(player.y_pos, SCREEN_HEIGHT - player.height))

            # Check if it's time to change the martian's position
            current_time = pygame.time.get_ticks()
            if current_time - last_martian_change > self.MARTIAN_CHANGE_INTERVAL:
                last_martian_change = current_time
                enemy_0.x_pos = random.randint(0, SCREEN_WIDTH - enemy_0.width)
                enemy_0.y_pos = random.randint(0, SCREEN_HEIGHT - enemy_0.height)

            # Draw objects
            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image, (0, 0))
            player.draw(self.game_screen)
            enemy_0.draw(self.game_screen)
            dest.draw(self.game_screen)

            # Check for collisions
            if player.detect_collision(enemy_0):
                yes_rect, no_rect = self.draw_popup("Play Again?")
                waiting_for_answer = True
                while waiting_for_answer:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return False  # Signal to completely exit the game
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if yes_rect.collidepoint(event.pos):
                                return True  # Restart the game
                            elif no_rect.collidepoint(event.pos):
                                return False  # Exit the game
                    pygame.display.update()
            elif player.detect_collision(dest):
                is_game_over = True
                did_win = True
                text = self.font.render('You Win!', True, BLACK_COLOR)
                self.game_screen.blit(text, (275, 350))

            pygame.display.update()
            clock.tick(self.TICK_RATE)

        # Wait for a moment before restarting or quitting
        pygame.time.wait(2000)

        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return False

# Main game loop
if __name__ == "__main__":
    new_game = Game('assets/tharsis_region.jpg', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
    play_again = True
    while play_again:
        play_again = new_game.run_game_loop(1)

pygame.quit()

```


## Challenges
1. Modify the martian's disappearing interval and experiment with different timings
2. Add a score system that increases the longer the player survives
3. Create a more elaborate menu with multiple options (e.g., Start Game, Settings, Quit)
4. Implement difficulty levels that affect the martian's behavior

## Learning Outcomes
- Understand how to create time-based events in games
- Learn to manage different game states
- Gain experience in creating simple game menus
- Practice resetting and managing game objects for replay functionality
