import pygame
from projectile import Projectile
from projectile_green import ProjectileGreen
from projectile_crit import ProjectileCrit
import animation
import random


# class of the player.
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.crit = 30
        self.velocity = 2.5
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 500
        self.all_projectile = pygame.sprite.Group()

    def update_animation(self):
        self.animate(loop=False, speed=1)

    # function of the player health bar.
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (153, 53, 53), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (48, 232, 19), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    # function to apply damage to the player and stop the game if it has no life left.
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    # function for launch a projectile.
    def launch_projectile(self):
        self.start_animation()
        if random.uniform(0, 100) <= 3:
            self.all_projectile.add(ProjectileGreen(self))
        elif random.uniform(0, 100) <= 20:
            self.all_projectile.add(ProjectileCrit(self))
        else:
            self.all_projectile.add(Projectile(self))

    # if the player is not blocked by a monste, make him move to the right.
    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity

    # function to make move the player to the left.
    def move_left(self):
        self.rect.x += -self.velocity
