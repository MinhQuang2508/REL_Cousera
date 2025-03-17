import pygame
import sys
import numpy as np
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(WHITE)

# Task 1: Create the game board
def create_board():
    return np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_lines():
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Task 2: Handle user input and turns
def mark_square(board, row, col, player):
    board[row][col] = player

def available_square(board, row, col):
    return board[row][col] == 0

# Task 3: Check for a win
def check_win(board, player):
    for row in range(BOARD_ROWS):
        if np.all(board[row, :] == player):
            return True
    for col in range(BOARD_COLS):
        if np.all(board[:, col] == player):
            return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Task 4: Draw game elements
def draw_figures(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                animate_circle(col, row)
            elif board[row][col] == 2:
                animate_cross(col, row)

# Task 5: Handle game restart
def restart_game(board):
    screen.fill(WHITE)
    draw_lines()
    board.fill(0)

# Task 6: Animate game elements
def animate_circle(col, row):
    center = (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE / 2))
    for r in range(0, CIRCLE_RADIUS + 5, 5):
        pygame.draw.circle(screen, BLUE, center, r, CIRCLE_WIDTH)
        pygame.display.update()
        pygame.time.delay(30)

def animate_cross(col, row):
    start_pos1 = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
    end_pos1 = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
    start_pos2 = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
    end_pos2 = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
    
    for i in range(0, CROSS_WIDTH + 5, 5):
        pygame.draw.line(screen, RED, start_pos1, end_pos1, i)
        pygame.display.update()
        pygame.time.delay(30)
        pygame.draw.line(screen, RED, start_pos2, end_pos2, i)
        pygame.display.update()
        pygame.time.delay(30)

# Initialize game
draw_lines()
board = create_board()
player = 1
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col, row = x // SQUARE_SIZE, y // SQUARE_SIZE
            if available_square(board, row, col):
                mark_square(board, row, col, player)
                draw_figures(board)
                if check_win(board, player):
                    print(f"Player {player} wins!")
                    pygame.time.wait(2000)
                    restart_game(board)
                player = 3 - player  # Switch player
    pygame.display.update()

pygame.quit()
sys.exit()
