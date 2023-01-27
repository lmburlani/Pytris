import pygame
import random

# Define as cores das peças
colors = {
    'I': (0, 255, 255),
    'J': (0, 0, 255),
    'L': (255, 165, 0),
    'O': (255, 255, 0),
    'S': (0, 255, 0),
    'T': (128, 0, 128),
    'Z': (255, 0, 0)
}

# Define as formas das peças
shapes = {
    'I': [[1, 1, 1, 1]],
    'J': [[1, 0, 0], [1, 1, 1]],
    'L': [[0, 0, 1], [1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'Z': [[1, 1, 0], [0, 1, 1]]
}

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
width, height = 400, 800

# Cria a janela
screen = pygame.display.set_mode((width, height))

# Define o título da janela
pygame.display.set_caption('Tetris')

# Define o tamanho das peças
block_size = 20

# Define a posição inicial das peças
start_x = width // 2 - block_size
start_y = 0

# Define a velocidade de queda das peças
fall_speed = 500

# Define o tempo atual e o tempo anterior
current_time = pygame.time.get_ticks()
prev_time = current_time

# Define a peça atual e a próxima peça
current_piece = random.choice(list(shapes.keys()))
next_piece = random.choice(list(shapes.keys()))

# Define as coordenadas da peça atual
x, y = start_x, start_y

# Define o loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Pega o tempo atual
    current_time = pygame.time.get_ticks()

    # Verifica se é hora de mover a peça para baixo
    if current_time - prev_time > fall_speed:
    prev_time = current_time
    y += block_size

# Preenche a tela com preto
screen.fill((0, 0, 0))

# Desenha a peça atual na tela
for i in range(len(shapes[current_piece])):
    for j in range(len(shapes[current_piece][i])):
        if shapes[current_piece][i][j]:
            pygame.draw.rect(screen, colors[current_piece], (x + j * block_size, y + i * block_size, block_size, block_size))

# Desenha a próxima peça na tela
for i in range(len(shapes[next_piece])):
    for j in range(len(shapes[next_piece][i])):
        if shapes[next_piece][i][j]:
            pygame.draw.rect(screen, colors[next_piece], (width - block_size * 5 + j * block_size, i * block_size, block_size, block_size))

# Atualiza a tela
pygame.display.flip()

# Define a condição de parada do jogo
if y > height:
    running = False

# Finaliza o jogo
pygame.quit()
