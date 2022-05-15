import pygame as pg, numpy
from sprite import Sprite
class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("player/zeku.png", startx, starty)
        self.stand_image = self.image
        self.jump_image = self.image
        #self.walk_cycle = [pg.image.load(f"p1_walk{i:0>2}.png") for i in range(1,12)]
        self.animation_index = 0
        self.facing_left = False
        self.speed = 4
        self.jumpspeed = 20
        self.vsp = 0
        self.gravity = 1
        self.min_jumpspeed = 4
        self.prev_key = pg.key.get_pressed()

    def walk_animation(self):
        self.image = self.stand_image
        if self.facing_left:
            self.image = pg.transform.flip(self.image, True, False)

        '''if self.animation_index < len(self.walk_cycle)-1:
            self.animation_index += 1
        else:
            self.animation_index = 0'''

    def jump_animation(self):
        self.image = self.jump_image
        if self.facing_left:
            self.image = pg.transform.flip(self.image, True, False)

    def update(self, boxes):
        hsp = 0
        onground = self.check_collision(0, 1, boxes)
        # check keys
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.facing_left = True
            self.walk_animation()
            hsp = -self.speed
        if key[pg.K_d]:
            self.facing_left = False
            self.walk_animation()
            hsp = self.speed

        if key[pg.K_SPACE] and onground:
            self.vsp = -self.jumpspeed

        # variable height jumping
        if self.prev_key[pg.K_SPACE] and not key[pg.K_SPACE]:
            if self.vsp < -self.min_jumpspeed:
                self.vsp = -self.min_jumpspeed

        self.prev_key = key

        # gravity
        if self.vsp < 10 and not onground:  # 9.8 rounded up
            self.jump_animation()
            self.vsp += self.gravity

        if onground and self.vsp > 0:
            self.vsp = 0

        # movement
        self.move(hsp, self.vsp, boxes)

    def move(self, x, y, boxes):
        dx = x
        dy = y
        while self.check_collision(0, dy, boxes):
            dy -= numpy.sign(dy)
        while self.check_collision(dx, dy, boxes):
            dx -= numpy.sign(dx)
        self.rect.move_ip([dx, dy])

    def check_collision(self, x, y, grounds):
        self.rect.move_ip([x, y])
        collide = pg.sprite.spritecollideany(self, grounds)
        self.rect.move_ip([-x, -y])
        return collide