import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Connect 4")

# Create a grid of buttons for the board
board = []
for i in range(6):
    row = []
    for j in range(7):
        button = tk.Button(root, text=" ", width=12, height=6)
        button.grid(row=i, column=j)
        row.append(button)
    board.append(row)

# Define click handlers for the buttons
def button_click(row, col):
    print("Button clicked:", row, col)

for i in range(6):
    for j in range(7):
        board[i][j].config(command=lambda row=i, col=j: button_click(row, col))

# Create a menu for selecting difficulty level and algorithm type
menu = tk.Menu(root)
root.config(menu=menu)

difficulty_menu = tk.Menu(menu)
menu.add_cascade(label="Difficulty Level", menu=difficulty_menu)
difficulty_menu.add_command(label="1")
difficulty_menu.add_command(label="2")
difficulty_menu.add_command(label="3")
difficulty_menu.add_command(label="4")
difficulty_menu.add_command(label="5")

algorithm_menu = tk.Menu(menu)
menu.add_cascade(label="Algorithm Type", menu=algorithm_menu)
algorithm_menu.add_command(label="Minimax")
algorithm_menu.add_command(label="Alpha-beta pruning")

# Display the GUI and run the main loop
root.mainloop()




------------------------------------------------------------------------------------------------

from connect4 import Connect4
import pygame
import sys
import random
import math

rand = random.Random()

class Connect4_GUI(Connect4):

    BLUE = (0, 0, 255)
    LIGHT_BLUE = (0, 0, 128)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    SQUARESIZE = 100
    WIDTH = Connect4.NUM_COLS*SQUARESIZE
    HEIGHT = (1+Connect4.NUM_ROWS)*SQUARESIZE
    SIZE = (WIDTH, HEIGHT)
    RADIUS = int(SQUARESIZE/2 - 5)
    SCREEN = pygame.display.set_mode(SIZE)

    def draw_board(self):
        for c in range(self.NUM_COLS):
            for r in range(self.NUM_ROWS):
                loc_size = (c*self.SQUARESIZE, (r+1)*self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE)
                pygame.draw.rect(self.SCREEN, self.BLUE, loc_size)
                loc = (int((c+0.5)*self.SQUARESIZE), int((r+1.5)*self.SQUARESIZE))
                pygame.draw.circle(self.SCREEN, self.BLACK, loc, self.RADIUS)
        
        for c in range(self.NUM_COLS):
            for r in range(self.NUM_ROWS):		
                if self.board[r][c] == 1:
                    loc = (int((c+0.5)*self.SQUARESIZE), int((r+1.5)*self.SQUARESIZE))
                    pygame.draw.circle(self.SCREEN, self.RED, loc, self.RADIUS)
                elif self.board[r][c] == -1: 
                    loc = (int((c+0.5)*self.SQUARESIZE), int((r+1.5)*self.SQUARESIZE))
                    pygame.draw.circle(self.SCREEN, self.YELLOW, loc, self.RADIUS)
        pygame.display.update()

    def run_game(self):
        pygame.init()
        myfont = pygame.font.SysFont("monospace", 75)
        self.draw_board()
        pygame.display.update()


        moves = self.get_avail_moves()
        player = 1 # first player is always 1
        human_player = rand.choice([1, -1])
        winner = False
        exit_flag = False
        while moves != [] and winner == False and exit_flag == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_flag = True

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.SCREEN, self.BLACK, (0,0, self.WIDTH, self.SQUARESIZE))
                    posx = event.pos[0]
                    if player ==  1:
                        pygame.draw.circle(self.SCREEN, self.RED, (posx, int(self.SQUARESIZE/2)), self.RADIUS)
                    else: 
                        pygame.draw.circle(self.SCREEN, self.YELLOW, (posx, int(self.SQUARESIZE/2)), self.RADIUS)
                    
                    pygame.display.update()

                # wait for player input
                if player == human_player and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.SCREEN, self.BLACK, (0,0, self.WIDTH, self.SQUARESIZE))
                    posx = event.pos[0]
                    move = int(math.floor(posx/self.SQUARESIZE))
                    if move in moves:
                        self.make_move(move)
                        self.draw_board()
                        if self.get_winner():
                            if human_player == 1:
                                label = myfont.render("Human wins!!!", 1, self.RED)
                            else:
                                label = myfont.render("Human wins!!!", 1, self.YELLOW)
                            self.SCREEN.blit(label, (40,10))
                            self.draw_board()
                            winner = True
                            break
                            
                        player = -player

                # Ask for Player 2 Input
                elif player == -human_player:			
                    move =  rand.choice(moves)
                    if move in moves:
                        self.make_move(move)
                        self.draw_board()
                        if self.get_winner():
                            if player == 1:
                                label = myfont.render("Human loses!", 1, self.RED)
                            else:
                                label = myfont.render("Human loses!", 1, self.YELLOW)
                            self.SCREEN.blit(label, (40,10))
                            self.draw_board()
                            winner = True
                            break
                            
                        player = -player
            moves = self.get_avail_moves()
        if winner == False and moves == []:
            label = myfont.render("It's a Draw :/", 1, self.LIGHT_BLUE)
            self.SCREEN.blit(label, (40,10))
            self.draw_board()
        while exit_flag == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_flag = True
        pygame.quit()

def main():
    my_game = Connect4_GUI()
    my_game.run_game()

if __name__ == "__main__":
    main()
