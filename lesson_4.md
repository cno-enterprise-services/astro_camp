# Lesson 4: Advanced Features - Disappearing Martian and Play Again Menu
Welcome to Lesson 4 of creating your Mars Rover game! In this lesson, you'll learn how to improve the game some making the rover move using rotation and forward and backward commands as well as add a moving Martian mechanic. By the end of this lesson, you'll have an improved game.

## Learning Objectives
By the end of this lesson, students will be able to:
1. Implement a disappearing and reappearing game object (Martian)
2. Create a simple play again menu using Pygame
3. Manage game states for restarting or exiting the game

## Step-by-Step Tutorial

### Step 1: Implementing the Disappearing Martian

We'll use Pygame's time module to make the Martian disappear and reappear:

```python
MARTIAN_CHANGE_INTERVAL = 6000  # 6 seconds in milliseconds

# Inside the game loop
current_time = pygame.time.get_ticks()
if current_time - last_martian_change > self.MARTIAN_CHANGE_INTERVAL:
    last_martian_change = current_time
    martian.x_pos = random.randint(0, SCREEN_WIDTH - martian.width)
    martian.y_pos = random.randint(0, SCREEN_HEIGHT - martian.height)
```

### Step 2: Creating the Play Again Menu

We'll add a method to draw a popup menu:

```python
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
```

### Step 3: Implementing Game Logic for Restarting or Exiting

We'll modify the collision detection to show the play again menu:

```python
if rover.detect_collision(martian):
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
```

## Challenges

1. Modify the Martian's disappearing interval and experiment with different timings.
2. Add a score system that increases the longer the player survives.
3. Create multiple Martians that appear and disappear at different intervals.

## Reflection Questions

1. How does the use of time in games enhance the player experience?
2. What other features could we add to make the game more challenging or interesting?
3. How might we use similar popup menus for other game features (e.g., settings, instructions)?
