from pygame.sprite import Sprite
from constants import *
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Player.png")
        self.rect = self.image.get_rect(centerx=SCREEN_WIDTH / 2, bottom=SCREEN_HEIGHT)
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 10
        self.mask = pygame.mask.from_surface(self.image)
    def draw(self):
        screen.blit(self.image, self.rect)