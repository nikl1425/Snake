import pygame

WIDTH = 600
HEIGHT = 600
FPS = 30
clock = pygame.time.Clock()
forest_green = (161, 40, 48)


class Player:
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.speed = 3


def main():
    pygame.init()
    background = pygame.image.load('Assets/background.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    player = Player(0, 0, WIDTH/20, HEIGHT/20, "right")

    running = True

    def draw():
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, forest_green, (player.x, player.y, player.width, player.height))

        pygame.display.flip()

    def player_movement():
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

    while running:
        clock.tick(FPS)
        print("runs")

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

        draw()


if __name__ == "__main__":
    main()
