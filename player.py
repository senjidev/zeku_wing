import pygame as pg
from sprite import Sprite
class Player(Sprite):
	def __init__(self, startx, starty):
		super().__init__("player/zeku.png",startx,starty)
		self.speed = 4
		self.idle = self.image
		self.gravity = 1
		self.jumpspeed = 20
		self.min_jumpspeed = 3
		self.prev_key = pg.key.get_pressed()
		self.vsp = 0 #vert speed is in init for variable persistance
		self.facing_left = False
		#anim
		self.stand_image = self.image
		#self.jump_image = pg.image.load("path/jump_anim_01.png")
		#self.walk_cycle = [pg.image.load(f"walk_anim_o1.png") for i in range(1,12)]
		self.animation_index = 0
	def update(self, tiles):
		hsp = 0 #horizontal speed
		onground = self.check_collision(0,1,tiles)
		# check keys
		key = pg.key.get_pressed()
		if key[pg.K_a]:
			self.facing_left = True
			self.walk_animation()
			hsp = -self.speed
		elif key[pg.K_d]:
			self.facing_left = False
			self.walk_animation()
			hsp = self.speed
		#respawn
		if self.rect.y > 500:
			self.rect.y = 20
			self.rect.x = 100
		#jump key
		if key[pg.K_SPACE] and onground:
			self.vsp = -self.jumpspeed
		#variable height jumping
		if self.prev_key[pg.K_SPACE] and not key[pg.K_SPACE]:
			if self.vsp < -self.min_jumpspeed:
				self.vsp = -self.min_jumpspeed
		self.prev_key = key
		"""GRAVITY"""
		if self.vsp < 10 and not onground:
			#self.jump_animation()
			self.vsp += self.gravity
		if self.vsp > 0 and onground:
			self.vsp = 0
		"""MOVEMENT"""
		self.move(hsp, self.vsp)
	def walk_animation(self):
		self.image = self.stand_image
		if self.facing_left:
			self.image = pg.transform.flip(self.image,True,False)
		"""if self.animation_index < len(self.walk_cycle)-1:
			self.animation_index += 1
		else:
			self.animation_index = 0"""
	def jump_animation(self):
		self.image = self.jump_image
		if self.facing_left:
			pass
	def move(self,x,y):
		self.rect.move_ip([x,y])
	def check_collision(self, x, y, grounds):
		self.rect.move_ip([x, y])
		collide = pg.sprite.spritecollideany(self, grounds)
		self.rect.move_ip([-x, -y])
		return collide
