import pygame
from comet import Comet


# class of the comet fall event.
class CometFallEvent:

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False

    #
    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):
        for i in range(1, 40):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monster) == 0:
            self.meteor_fall()
            self.fall_mode = True

    def update_bar(self, surface):
        self.add_percent()
        pygame.draw.rect(surface, (60, 60, 60), [0, surface.get_height() - 10, surface.get_width(), 10])
        pygame.draw.rect(surface, (190, 190, 190), [0, surface.get_height() - 10, (surface.get_width() / 100) * self.percent, 10])
