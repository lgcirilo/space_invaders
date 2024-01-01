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


def draw_player(x: float, y: float) -> None:
    screen.blit(player_img, (x, y))


# not currently used
# def has_reached_border(player_x):
#     return player_x >= 800 - player_img.get_width() or player_x <= 0

def change_vector_direction():
    global x_vector
    x_vector = x_vector * -1


# game loop
running = True


def move_left(player_x: int) -> None:
    if x_vector > 0:
        change_vector_direction()
    player_x = player_x + x_vector

    return player_x


def move_right(player_x: int) -> None:
    if x_vector < 0:
        change_vector_direction()
    player_x = player_x + x_vector

    return player_x


def set_player_x(param):
    global player_x
    player_x = param


def move() -> None:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            set_player_x(move_left(player_x))
        if event.key == pygame.K_RIGHT:
            set_player_x(move_right(player_x))


def quit_on_user_request():
    global running
    if event.type == pygame.QUIT:
        running = False


# main loop
while running:
    # screen background color in RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        quit_on_user_request()

        move()

    # draws player on screen
    draw_player(player_x, player_y)
    # this line is needed to maek the screen show the background color we set with screen.fill
    pygame.display.update()

# if event.type == pygame.QUIT:
