import pygame
import random
import animation


# class of the monster.
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0, health=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100 + health
        self.attack = 0.1
        self.rect = self.image.get_rect()
        self.rect.x = 1080 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.velocity = random.uniform(0.8, 2)
        self.start_animation()

    # function to apply damage to the monster and make it respawn if it has no life left.
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.record_temp += 1
            self.rect.x = 1080 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.uniform(0.3, 1.2)

            if self.game.comet_event.is_full_loaded():
                self.game.all_monster.remove(self)
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True, speed=self.velocity)

    # function of the monster health bar.
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (153, 53, 53), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (48, 232, 19), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    # function to move the monster if the monster is not blocked by the player.
    def forward(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)


class Mummy(Monster):
    
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))


class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 300
        self.max_health = 300