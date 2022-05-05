import pygame as pg
from sprite import Sprite

class Player(Sprite):
	def __init__(self, startx, starty):
		super().__init__("player/zeku.png",startx,starty)
		self.speed = 4
		self.idle = self.image

	def update(self):
		#input monitoring
		key = pg.key.get_pressed()
		if key[pg.K_a]:
			self.move(-self.speed,0)
		elif key[pg.K_d]:
			self.move(self.speed,0)

	def move(self, x, y):
		self.rect.move_ip([x,y])