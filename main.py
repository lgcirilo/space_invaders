import pygame

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
clock.tick(60)
# create screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# player
player_img = pygame.image.load("player.png")
player_x = 370
player_y = 480
# x_vector = 3
playerX_change = 0


def player(player_x: float, player_y: float) -> None:
    screen.blit(player_img, (player_x, player_y))


def has_reached_border() -> bool:
    return player_x >= 800 - player_img.get_width() or player_x <= 0


# game loop
running = True
while running:
    # screen background color in RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # update player position
    if has_reached_border():
        playerX_change = player_img.get_rect()

    player_x += playerX_change
    # draws player on screen
    player(player_x, player_y)
    # this line is needed to make the screen show the background color we set with screen.fill
    pygame.display.update()
