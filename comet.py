import pygame
import random
from monster import Mummy, Alien


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.x += random.randint(20, 1000)
        self.rect.y += - random.randint(0, 3000)
        self.comet_event = comet_event

    # function to remove a comete.
    def remove(self):
        self.comet_event.all_comets.remove(self)

        # if it's the last comet spawn three monsters, reset the charging bar and desactive the comet fall event.
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.percent = 0
            self.comet_event.fall_mode = False
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Alien)

    # function to make fall the comet.
    def fall(self):
        self.rect.y += random.uniform(1, 3)
        if self.rect.y >= 600:
            self.remove()

        #
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_player):
            self.remove()
            self.comet_event.game.player.damage(30)
