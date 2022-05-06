import pygame as pg
class Sprite(pg.sprite.Sprite):
   def __init__(self, image, startx, starty):
      super().__init__()
      self.image = pg.image.load(image)
      self.rect = self.image.get_rect()
      self.center = [startx, starty]
      self.rect.center = self.center
   def update(self):
      pass
   
   def draw(self, surf):
      surf.blit(self.image,self.rect)
