from pygame.sprite import Sprite
from constants import *
class Fruit(Sprite):
    def __init__(self, x : int, y : int, group : pygame.sprite.Group):
        super().__init__()
        self.image = pygame.image.load("assets/Apple.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.price = 1
        self.ptext = GAME_FONT.render(f"{self.price}", True, (255,0,0))
        self.prect = self.ptext.get_rect(bottom=self.rect.top - 2, centerx=self.rect.centerx)
        self.gravity = 5
        group.add(self)
    def update(self, money : int):
        self.rect.y += self.gravity
        self.mask = pygame.mask.from_surface(self.image)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()
            if money:
                live_lose_sound.play()
                money -= 1
        self.ptext = GAME_FONT.render(f"{self.price}", True, (255,0,0))
        self.prect = self.ptext.get_rect(bottom=self.rect.top - 2, centerx=self.rect.centerx)
        screen.blit(self.ptext, self.prect)
        return money