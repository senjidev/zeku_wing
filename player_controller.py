import pygame as pg

def move(Player):

	if Player.moving_right:
		Player.x += 50

	if Player.moving_left:
		Player.x -= 50
