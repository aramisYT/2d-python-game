import pygame
import random


# classs of the projectile.
class ProjectileCrit(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 5
        self.image = pygame.image.load("assets/projectile_crit.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    # function to make rotate the projectile.
    def rotate(self):
        self.angle += 4
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    # function to remove the projectile.
    def remove(self):
        self.player.all_projectile.remove(self)

    # function to make move the projectile forward.
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # if a projectile hits a monster, it takes damage and the projectile disappears.
        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            self.remove()
            monster.damage(self.player.attack + self.player.crit)

        # if the projectile pass the window, remove the projectile with the function remove.
        if self.rect.x > 1080:
            self.remove()
