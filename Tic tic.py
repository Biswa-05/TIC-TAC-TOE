import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)  # For draw message

# Font
font = pygame.font.SysFont(None, 40)

# Board dimensions
board_size = 3
cell_size = width // board_size

# Create an empty board
board = [['' for _ in range(board_size)] for _ in range(board_size)]

# Current player
current_player = 'X'

# Game over flag
game_over = False

def draw_board():
    """Draws the Tic-Tac-Toe board on the screen."""
    screen.fill(white)
    for i in range(1, board_size):
        # Draw horizontal lines
        pygame.draw.line(screen, black, (0, i * cell_size), (width, i * cell_size), 3)
        # Draw vertical lines
        pygame.draw.line(screen, black, (i * cell_size, 0), (i * cell_size, height), 3)

def draw_markers():
    """Draws the 'X' and 'O' markers on the board."""
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 'X':
                pygame.draw.line(screen, red, (col * cell_size + 10, row * cell_size + 10), 
                                 ((col + 1) * cell_size - 10, (row + 1) * cell_size - 10), 5)
                pygame.draw.line(screen, red, ((col + 1) * cell_size - 10, row * cell_size + 10), 
                                 (col * cell_size + 10, (row + 1) * cell_size - 10), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, green, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), 
                                  cell_size // 2 - 5, 5)

def check_win():
    """Checks for a winning condition."""
    # Check rows
    for row in range(board_size):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '':
            return board[row][0]  # Return the winning player ('X' or 'O')

    # Check columns
    for col in range(board_size):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] or 
        board[0][2] == board[1][1] == board[2][0]) and board[1][1] != '':
        return board[1][1]

    return None

def check_draw():
    """Checks for a draw."""
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == '':
                return False
    return True

def get_mouse_position():
    """Gets the row and column of the clicked cell."""
    x, y = pygame.mouse.get_pos()
    row = y // cell_size
    col = x // cell_size
    return row, col

def display_game_over_message(winner):
    """Displays the game over message on the screen."""
    if winner:
        message = f"Player {winner} wins!"
        color = red if winner == 'X' else green
    else:
        message = "It's a draw!"
        color = blue

    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            row, col = get_mouse_position()
            if board[row][col] == '':
                board[row][col] = current_player

                winner = check_win()
                if winner:
                    game_over = True
                elif check_draw():
                    game_over = True

                current_player = 'O' if current_player == 'X' else 'X'

    draw_board()
    draw_markers()

    if game_over:
        display_game_over_message(winner)

    pygame.display.update()

pygame.time.delay(3000)
pygame.quit()
