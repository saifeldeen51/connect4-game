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
