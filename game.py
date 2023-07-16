import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent


# class of the game.
class Game:

    def __init__(self):
        self.record_temp = 0
        self.is_playing = False
        self.monster = Monster
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.comet_event = CometFallEvent(self)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}

    # function start, start the game and spawn two monster.
    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    # function game over, if the player has no life left, go to the menu, reset the player life,
    # remove the monsters and check if a new record was reached.
    def game_over(self):
        self.file = open("record.txt", 'r')
        self.record = int(self.file.read())
        self.file.close()
        if self.record_temp > self.record:
            self.file = open("record.txt", 'w')
            self.file.write(str(self.record_temp))
            self.file.close()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.percent = 0
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.fall_mode = False
        self.is_playing = False
        self.player.rect.x = 50
        self.player.rect.y = 500

    # function update,
    def update(self, screen):

        # draw the player.
        screen.blit(self.player.image, self.player.rect)

        # draw the projectile.
        self.player.all_projectile.draw(screen)

        # draw the monster
        self.all_monster.draw(screen)

        self.comet_event.all_comets.draw(screen)

        # start the function "update_health_bar".
        self.player.update_health_bar(screen)

        # start the function "update_bar".
        self.comet_event.update_bar(screen)

        self.player.update_animation()

        # when a projectile is add, make it move.
        for projectile in self.player.all_projectile:
            projectile.move()

        # when a monster is add, make it move.
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # when a comet is add, make it fall.
        for comet in self.comet_event.all_comets:
            comet.fall()

        police = pygame.font.SysFont("arial_black", 30)
        image_texte = police.render("score : " + str(self.record_temp), 1, (10, 10, 10))
        screen.blit(image_texte, (0, 0))

        # make move the player if the key pressed is "d" or "a" and if the player is not to the limit of the window.
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < 1080:
            self.player.move_right()
        elif self.pressed.get(pygame.K_a) and self.player.rect.x > 0:
            self.player.move_left()

    # function to check for a collision.
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # function to spawn a monster.
    def spawn_monster(self, monster_class_name):
        self.all_monster.add(monster_class_name.__call__(self))
