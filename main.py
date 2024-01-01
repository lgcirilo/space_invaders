import pygame

# Initialize pygame
pygame.init()

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
x_vector = 3

def player():
    screen.blit(player_img, (player_x, player_y))

def bounce_player():
    global player_x
    global player_y
    global x_vector

    if has_reached_border(player_x):
        change_vector_direction()

    player_x = player_x + x_vector

    print(str(player_x))


def has_reached_border(player_x):
    return player_x >= 800 - player_img.get_width() or player_x <= 0

def change_vector_direction():
    global x_vector
    x_vector = x_vector * -1


# game loop
running = True
while running:
    # screen background color in RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draws player on screen
    player()
    bounce_player()
    # this line is needed to maek the screen show the background color we set with screen.fill
    pygame.display.update()


# if event.type == pygame.QUIT:

