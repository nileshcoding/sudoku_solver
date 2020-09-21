import pygame
from solver import solve, valid
import time
pygame.font.init()


grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("Sudoku Solver")

#Draw the Sudoku Grids
dif = 500/9
font1 = pygame.font.SysFont("comicsans", 40) 
font2 = pygame.font.SysFont("comicsans", 20)
color = (255,255,255)
for i in range (9): 
	for j in range (9): 
		if grid[i][j]!= 0: 
			pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1)) 
			text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0)) 
			screen.blit(text1, (i * dif + 15, j * dif + 15))
for i in range(10): 
	if i % 3 == 0 : 
		thick = 7
	else: 
		thick = 1
	pygame.draw.line(screen, color, (0, i * dif), (500, i * dif), thick) 
	pygame.draw.line(screen, color, (i * dif, 0), (i * dif, 500), thick)
pygame.display.update()