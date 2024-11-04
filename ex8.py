import random

### Minesweeper game ###

def minesweeper():
    grid_size = input("Select grid size: ")
    # while (type(grid_size) != int):
    #     print("!\nPlease enter an integer\n!")
    #     grid_size = input("Select grid size: ")

    
    ### Setup minefield
    minefield = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    random.sample()

minesweeper()