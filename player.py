import pygame
# Game config
WIDTH = 600
HEIGHT = 600
FPS = 1
SCORE = 0
clock = pygame.time.Clock()
red = (161, 40, 48)
lime = (0, 255, 0)
snake_body = []
x_back = 30
y_back = 30
intro_screen = False


class Player:
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.speed = 30
        self.body_parts = [pygame.Rect(self.x, self.y, self.width, self.height)]

    def player_movement(self):
        # change direction on input
        if self.direction == "right":
            self.x += self.speed
        if self.direction == "down":
            self.y += self.speed
        if self.direction == "up":
            self.y -= self.speed
        if self.direction == "left":
            self.x -= self.speed
        # prevent player from exiting screen
        if self.x + self.width/2 < 0:
            self.x = WIDTH
        if self.x > WIDTH:
            self.x = 0
        if self.y + self.height/2 < 0:
            self.y = HEIGHT
        if self.y > HEIGHT:
            self.y = 0

    def get_rect(self):
        box = pygame.Rect(self.x, self.y, self.width, self.height)
        return box

    def draw(self, window):
        for body_part in self.body_parts:
            pygame.draw.rect(window, red, body_part)
            print(body_part.x)

    def update(self):
        self.player_movement()
        self.body_parts.insert(0, pygame.Rect(self.x, self.y, self.width, self.height))
        self.body_parts.pop()