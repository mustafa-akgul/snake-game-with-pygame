import pygame, sys, random
from start_menu1 import main_menu
from ending_menu1 import ending_menu
screen_width = 600
screen_height = 600

gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

light_red = (255, 51, 51)
dark_red = (204, 0, 0)
food_color = (12, 5, 216)
snake_color = (102, 0, 102)

up = (0, -1)
down = (0, 1)
right = (1, 0)
left = (-1, 0)



class SNAKE:
    def __init__(self):
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.length = 1
        self.direction = random.choice([up, down, left, right])
        self.color = snake_color
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            rect = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, rect)

    def move(self):
        current = self.positions[0]
        x, y = self.direction
        new = ((current[0] + (x * gridsize)), (current[1] + (y * gridsize)))

        if new[0] in range(0, screen_width) and new[1] in range(0, screen_height) and not new in self.positions[1:]:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        else:
            ending_menu()
    

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)

    def turn(self, direction):
        if (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        else:
            self.direction = direction

class FOOD:
    def __init__(self):
        self.position = (0, 0)
        self.color = food_color
        self.random_position()

    def random_position(self):
        self.position = ((random.randint(0, int(grid_width) - 1)) * gridsize, random.randint(0, int(grid_height) - 1) * gridsize)

    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, rect)

def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                light = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, light_red, light)
            else:
                dark = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, dark_red, dark)

def main():
    main_menu()
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.SysFont("arial", 20)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    snake = SNAKE()
    food = FOOD()
    
    while True:
        clock.tick(20)
        snake.handle_keys()
        snake.move()

        if snake.positions[0] == food.position:
            ending_menu()
            snake.length += 1
            snake.score += 1
            food.random_position()

        screen.fill((5, 216, 75))
        drawGrid(surface)
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))

        score_text = font.render(f"Score: {snake.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.update()

main()