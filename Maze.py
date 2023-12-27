import pygame 
pygame.init()
width,height = 500,500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Game!")
white = (255, 255, 255)
black = (0, 0, 0)
maze = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, black, (col * 40, row * 40, 40, 40))
            else:
                pygame.draw.rect(screen, white, (col * 40, row * 40, 40, 40))
player_size = 40
player_x, player_y = 60, 40

def draw_player():
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_size, player_size))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_j:
            print("")
            

    screen.fill(white)
    draw_maze()
    draw_player()

    pygame.display.flip()