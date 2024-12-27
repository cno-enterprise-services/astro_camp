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

        rover = GameObject('assets/mars_rover_sprite.png', 375, 500, 50, 50)
        martian = GameObject('assets/martian_sprite.png', 20, 400, 50, 50)
        destination = GameObject('Assets/space_suit_1.png', 375, 50, 50, 80)

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
            rover.y_pos -= direction_y * level_speed
            rover.x_pos += direction_x * level_speed
            
            # Keep player within screen bounds
            rover.x_pos = max(0, min(martian.x_pos, SCREEN_WIDTH - martian.width))
            rover.y_pos = max(0, min(martian.y_pos, SCREEN_HEIGHT - martian.height))

            # Draw objects
            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image, (0, 0))
            rover.draw(self.game_screen)
            martian.draw(self.game_screen)
            destination.draw(self.game_screen)

            # Check for collisions
            if rover.detect_collision(martian):
                is_game_over = True
                did_win = False
                text = font.render('You Lose!', True, BLACK_COLOR)
                self.game_screen.blit(text, (275, 350))
            elif rover.detect_collision(destination):
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
