import pygame


class Berry:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def hitbox(self):
        box = pygame.Rect(self.x, self.y, self.width, self.height)
        return box


