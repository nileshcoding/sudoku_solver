import pygame
from solver import solve, valid
import time
pygame.font.init()
from functions import *
#default sudoku grid
grid = [ 
		[7, 8, 0, 4, 0, 0, 1, 2, 0], 
		[6, 0, 0, 0, 7, 5, 0, 0, 9], 
		[0, 0, 0, 6, 0, 1, 0, 7, 8], 
		[0, 0, 7, 0, 4, 0, 2, 6, 0], 
		[0, 0, 1, 0, 5, 0, 9, 3, 0], 
		[9, 0, 4, 0, 6, 0, 0, 0, 5], 
		[0, 7, 0, 3, 0, 0, 0, 1, 2], 
		[1, 2, 0, 0, 0, 7, 4, 0, 0], 
		[0, 4, 9, 2, 0, 6, 0, 0, 7] 
	]


run = True
while run:
	draw_grid(grid,screen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run =  False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			solve(grid)