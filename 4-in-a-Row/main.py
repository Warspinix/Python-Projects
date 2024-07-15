import numpy as np
import pygame as p
import sys

# initialise pygame
p.init()

green, blue, black, red, yellow, white, violet = (0, 255, 0), (0,0,255), (0,0,0), (255,0,0), (255,255,0), (255,255,255), (127,0,255)
rows, columns = 6, 7

def create_board():
        board = np.zeros((rows, columns))
        return board

def display_matrix(board):  # not a necessary function, only present to show a matrix representation of the game with each move
        print(np.flip(board, 0))

def is_valid_location(board, col):
        if board[rows - 1][col] == 0:
                return True
        return False

def get_next_open_row(board, col): # checks if a row-column entry is open, i.e = 0, i.e. not equal to 1 or 2
        for i in range(rows):
                if board[i][col] == 0:
                        return i

def drop_piece(board, row, col, piece):
        board[row][col] = piece

def winning_move(board, piece): # piece is either 1 or 2; 1 for red and 2 for yellow
        # Rows
        for i in range(rows):
                for j in range(columns-3):
                        if board[i][j] == piece and board[i][j + 1] == piece and board[i][j + 2] == piece and board[i][j + 3] == piece:
                                return True
        # Columns
        for i in range(rows-3):
                for j in range(columns):
                        if board[i][j] == piece and board[i+1][j] == piece and board[i+2][j] == piece and board[i+3][j] == piece:
                                return True
        # Positive Diagonals
        for i in range(rows - 3):
                for j in range(columns - 3):
                        if board[i][j] == piece and board[i + 1][j + 1] == piece and board[i + 2][j + 2] == piece and board[i + 3][j + 3] == piece:
                                return True
        # Negative Diagonals
        for i in range(3, rows):
                for j in range(columns - 3):
                        if board[i][j] == piece and board[i- 1][j + 1] == piece and board[i - 2][j + 2] == piece and board[i- 3][j + 3] == piece:
                                return True
        return False

def draw_game_board(): # draws the actual game board
        for i in range(rows):
                for j in range(columns):
                        p.draw.rect(screen, black, (j * square_size, i * square_size + square_size, square_size, square_size))
                        p.draw.circle(screen, white,(j * square_size + square_size // 2, i * square_size + square_size + square_size // 2),radius)

        for i in range(rows):
                for j in range(columns):
                        if board[i][j] == 1:
                                p.draw.circle(screen, red,(j * square_size + square_size // 2, height - (i * square_size + square_size // 2)),radius)
                        elif board[i][j] == 2:
                                p.draw.circle(screen, yellow,(j * square_size + square_size // 2, height - (i * square_size + square_size // 2)),radius)
                p.display.update()

# Calling function display_matrix
board = create_board()
display_matrix(board)

# define the size of one square of the screen
square_size = 100

# define width and height of board, pass as tuple to display.set_mode
width = columns * square_size
height = (rows + 1) * square_size  # another row for dropping the coins, and displaying the result
screen = p.display.set_mode((width, height))
p.display.set_caption("4 in a Row")

radius = int(square_size/2 - 5)

# Calling function draw_game_board
draw_game_board()

font = p.font.SysFont("Georgia", 75)

game_over = False
turn = 0

while not game_over:
        for event in p.event.get():
                if event.type == p.QUIT:
                        sys.exit()
                if event.type == p.MOUSEMOTION:
                        p.draw.rect(screen, black, (0, 0, width, square_size))  # top rectangle
                        x = event.pos[0]
                        if turn == 0:
                                p.draw.circle(screen, red, (x, int(square_size / 2)), radius)
                        else:
                                p.draw.circle(screen, yellow, (x, int(square_size / 2)), radius)
                p.display.update()
                if event.type == p.MOUSEBUTTONDOWN:
                        p.draw.rect(screen, black, (0, 0, width, square_size))
                        print(event.pos)
                        # Player 1 Input
                        if turn == 0:
                                x = event.pos[0]
                                col = int(x/square_size)
                                if is_valid_location(board, col):
                                        row = get_next_open_row(board, col)
                                        drop_piece(board, row, col, 1)
                                        if winning_move(board, 1):
                                                label = font.render("        Red Wins!", 1, red)
                                                screen.blit(label, (40, 10))
                                                game_over = True
                                else:
                                        continue

                        # Player 2 Input
                        else:
                                x = event.pos[0]
                                col = int(x/square_size)
                                if is_valid_location(board, col):
                                        row = get_next_open_row(board, col)
                                        drop_piece(board, row, col, 2)
                                        if winning_move(board, 2):
                                                label = font.render("     Yellow Wins!", 2, yellow)
                                                screen.blit(label, (40, 10))
                                                game_over = True
                                else:
                                        continue

                        display_matrix(board)
                        draw_game_board()

                        turn += 1
                        turn %= 2

                        if game_over:
                                p.time.wait(5000)  # milliseconds/ 5 seconds
