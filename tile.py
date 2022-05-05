import pygame as pg
from sprite import Sprite

class Tile(Sprite):
   def __init__(self, startx, starty):
      super().__init__("tiles/grass.png",startx,starty)
