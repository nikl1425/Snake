import pygame
from random import randrange
from player import Player
from berry import Berry

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
        player.draw(screen)
        if berry.hitbox().colliderect(player.get_rect()):
            berry.x = randrange(WIDTH-30)
            berry.y = randrange(HEIGHT-30)
        else:
            screen.blit(strawberry, (berry.x, berry.y))
        pygame.display.flip()

    def collision():
        print("collission")
        global SCORE
        box = player.get_rect()
        if box.colliderect(berry.hitbox()):
            SCORE += 1
            print(SCORE)
            berry.x = randrange(WIDTH - 30)
            berry.y = randrange(HEIGHT - 30)
            b1 = pygame.Rect(player.x, player.y, player.width, player.height)
            player.body_parts.append(b1)

        for x in player.body_parts[1:]:
            if player.body_parts[0].colliderect(x):
                print("what")



    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_d and player.direction != "left":
                    player.direction = "right"
                    print("right activated")
                if event.key == pygame.K_s and player.direction != "up":
                    player.direction = "down"
                if event.key == pygame.K_w and player.direction != "down":
                    player.direction = "up"
                if event.key == pygame.K_a and player.direction != "right":
                    player.direction = "left"

        player.update()
        collision()
        draw()




if __name__ == "__main__":
    main()
