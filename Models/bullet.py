import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ali_game):
        super().__init__()
        self.screen = ali_game.screen
        self.settings = ali_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_with, self.settings.bullet_heigth)
        self.rect.midtop = ali_game.ship.rect.midtop
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)