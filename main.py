import pygame
from random import randrange

WIDTH = 600
HEIGHT = 600
FPS = 30
SCORE = 0
clock = pygame.time.Clock()
red = (161, 40, 48)
lime = (0, 255, 0)


class Berry:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def hitbox(self):
        box = pygame.Rect(self.x, self.y, self.width, self.height)
        return box


class Player:
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.speed = 3
        self.rect = pygame.Rect(x, y, width, height)

    def hitbox(self):
        box = pygame.Rect(self.x, self.y, self.width, self.height)
        return box


def main():
    pygame.init()


    # ASSETS and OBJECTS
    background = pygame.image.load('Assets/background.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    strawberry = pygame.image.load('Assets/strawberry.png')
    strawberry = pygame.transform.scale(strawberry, (40, 40))
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    player = Player(0, 0, WIDTH/20, HEIGHT/20, "right")
    berry = Berry(randrange(WIDTH-30), randrange(HEIGHT-30), int(WIDTH/20), int(WIDTH/20))


    def draw():
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, red, (player.x, player.y, player.width, player.height))
        screen.blit(strawberry, (berry.x, berry.y))
        pygame.display.flip()

    def player_movement():
        # change direction on input
        if player.direction == "right":
            player.x += player.speed
        if player.direction == "down":
            player.y += player.speed
        if player.direction == "up":
            player.y -= player.speed
        if player.direction == "left":
            player.x -= player.speed
        # prevent player from exiting screen
        if player.x + player.width/2 < 0:
            player.x = WIDTH
        if player.x > WIDTH:
            player.x = 0
        if player.y + player.height/2 < 0:
            player.y = HEIGHT
        if player.y > HEIGHT:
            player.y = 0

    def collision():
        global SCORE
        box = player.hitbox()
        box2 = berry.hitbox()
        if box.colliderect(berry.hitbox()):
            SCORE += 1
            print(SCORE)
            berry.x = randrange(WIDTH - 30)
            berry.y = randrange(HEIGHT - 30)


    running = True
    while running:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_d:
                    player.direction = "right"
                if event.key == pygame.K_s:
                    player.direction = "down"
                if event.key == pygame.K_w:
                    player.direction = "up"
                if event.key == pygame.K_a:
                    player.direction = "left"
        player_movement()
        collision()
        draw()
        #print("collision: ", player.hitbox().x, " player rect: ", player.x)



if __name__ == "__main__":
    main()
