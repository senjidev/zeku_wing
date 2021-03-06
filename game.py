"""
#
	a platformer game lol
	developed by:
		zeku += black wing
#
"""

from pygame.locals import *
import pygame as pg, sys
from player import Player
from tile import Box

class Game():
	def __init__(self):
		super().__init__()
		pg.init()
		self.running = True
		self.WIDTH = 1000
		self.HEIGHT = 800
		self.FPS = 60
		self.bg = (0, 0, 0)
		self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
		self.clock = pg.time.Clock()
		self.run()
	def run(self):
		#create player
		player = Player(100,20)
		tiles = pg.sprite.Group()
		#draw tiles
		for t in range(0,self.WIDTH,16):
			tiles.add(Box(t,self.HEIGHT))
		#game loop
		while self.running:
			self.event_handler()
			pg.event.pump()
			self.screen.fill(self.bg)
			player.draw(self.screen)
			player.update(tiles)
			tiles.draw(self.screen)
			pg.display.flip()
			self.clock.tick(self.FPS)
	#event handler
	def event_handler(self):
		super().__init__()
		for event in pg.event.get():
			if event.type == QUIT:
				print(f"GAME CLOSED")
				self.running = False
				sys.exit()
if __name__ == "__main__":
	Game()
