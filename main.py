# lang = en

from game import Game
import pygame
import math
pygame.init()

clock = pygame.time.Clock()
FPS = 144

# some parameters for the window.
pygame.display.set_caption("shooter")
screen = pygame.display.set_mode((1080, 720))

# set the path of the backgrounds.
background = pygame.image.load("assets/bg.jpg")

# menu banner.
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# play button.
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# load the game class.
game = Game()

# loop of the game.
running = True
while running:

    # draw the background.
    screen.blit(background, (0, -200))

    # if the game start, start the "update" function.
    if game.is_playing:
        game.update(screen)

    # if the game not start, draw the banner, the button and the record.
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
        file = open("record.txt", 'r')
        record = str(file.read())
        file.close()
        police = pygame.font.SysFont("arial_black", 30)
        image_texte = police.render("records : " + record, 1, (10, 10, 10))
        screen.blit(image_texte, (440, 500))

    # update the window.
    pygame.display.flip()

    # pygame event manager.
    for event in pygame.event.get():

        # close the window and the program if the player quit the game
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # if a key is pressed set "game.pressed" on "True".
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # if the key pressed is space launch a projectile.
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        # if a key is release set "game.pressed" on "False".
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # if the player clicks on the play button, start the "start" function.
        elif event.type == pygame.MOUSEBUTTONDOWN and not game.is_playing:
            if play_button_rect.collidepoint(event.pos):
                game.start()

    clock.tick(FPS)