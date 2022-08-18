import pygame
from settings import *
from player import Player
from overlay import Overlay
from sprites import Generic


class Level:

    def __init__(self):

        #get display surface
        self.display_surface = pygame.display.get_surface()

        #sprite groups
        self.all_sprites = CameraGroup()

        self.setup()
        self.overlay = Overlay(self.player)


    def setup(self):
        self.player = Player((960,540), self.all_sprites)
        Generic(    pos = (0,0), 
                    surf = pygame.image.load('../Python-Game/graphics/world/ground.png').convert_alpha(), 
                    groups = self.all_sprites,
                    z = LAYERS['ground']
        )

    def run(self,dt):
        self.display_surface.fill("black")
        self.all_sprites.custom_draw()
        self.all_sprites.update(dt)

        self.overlay.display()


class CameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()

    def custom_draw(self):
        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    self.display_surface.blit(sprite.image, sprite.rect)