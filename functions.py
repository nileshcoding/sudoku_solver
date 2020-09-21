import pygame
pygame.font.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Sudoku Solver")
def draw_grid(grid,screen):
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
            else:
                pygame.draw.rect(screen,(255,0,0),(i * dif, j * dif, dif + 1, dif + 1))

    for i in range(10): 
        if i % 3 == 0 : 
            thick = 7
        else: 
            thick = 1
        pygame.draw.line(screen, color, (0, i * dif), (500, i * dif), thick) 
        pygame.draw.line(screen, color, (i * dif, 0), (i * dif, 500), thick)
    pygame.display.update()