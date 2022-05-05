from pygame.locals import *
import pygame as pg, sys

from player import Player
from tile import Tile

class Game():
	def __init__(self):
		super().__init__()
		pg.init()
		self.running = True
		self.WIDTH = 400
		self.HEIGHT = 300
		self.FPS = 60
		self.bg = (0, 0, 0)
		self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
		self.clock = pg.time.Clock()
		self.run()
	def run(self):
		#create player
		player = Player(100,200)
		tiles = pg.sprite.Group()
		#draw tiles
		for t in range(0,400,16):
			tiles.add(Tile(t,300))
			
		#game loop
		while self.running:
			pg.event.pump()
			player.update()
			self.screen.fill(self.bg)
			player.draw(self.screen)
			tiles.draw(self.screen)
			pg.display.flip()
			self.clock.tick(self.FPS)

			
if __name__ == "__main__":
	Game()
