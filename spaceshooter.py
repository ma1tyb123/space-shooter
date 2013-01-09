#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

pygame.mouse.set_visible(0)

ship = pygame.image.load("images/SHIP.png")
shoot = pygame.image.load("images/BULLET.png")
enemyrect = pygame.image.load("images/BULLET.png")
shootnum = 5
shoot_y = 0
enemyposx = screen.get_width()/2 
enemyposy = 50

ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2

while True:
	clock.tick(60)
	screen.fill((0,200,240))
	x , y = pygame.mouse.get_pos()
	screen.blit(ship, (x - ship.get_width()/2, ship_top))
	screen.blit(enemyrect , (enemyposx , enemyposy ))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			shoot_y = screen.get_height() - ship.get_height()
			shoot_x = x - ship.get_width()/2 /2 /2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_0:
			shootnum = 5
		#these events change the speed of the bullet
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
			shootnum = 10
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
			shootnum = 20
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
			shootnum = 30
	if shoot_y > 0:
		screen.blit(shoot, (shoot_x, shoot_y))
		shoot_y -= shootnum
	pygame.display.update()