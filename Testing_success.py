import random

def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

def add_random_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while (mat[r][c] != 0):
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2

def current_state_game(mat):
    
    #whether 2048 is present or not
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048):
                return 'YOU WON'
    
    #whether empty cell is present or not
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0):
                return 'GAME IS NOT OVER'
    
    #whether there are any cells that could have consecutive elements to be same in 3 X 3
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i][j + 1] or mat[i][j] == mat[i + 1][j]):
                return 'GAME IS NOT OVER'
    
    #whether any last row elements are consecutive and could merge
    for j in range(3):
        if (mat[3][j] == mat[3][j + 1]):
            return 'GAME IS NOT OVER'
    
    #whether any last column elements are consecutive and could merge
    for i in range(3):
        if (mat[i][3] == mat[i + 1][3]):
            return 'GAME IS NOT OVER'
    
    #there is no movement 
    return 'LOST'

def compress(mat):
    new_grid = []
    changed = False
    for i in range(4):
        new_grid.append([0]*4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if (mat[i][j] != 0):
                new_grid[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos = pos + 1
    return new_grid,changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if (mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):
                mat[i][j] = 2*mat[i][j]
                mat[i][j + 1] = 0
                changed = True
    return mat,changed

def reverse(mat):
    new_grid = [[], [], [], []]
    for i in range(4):
        for j in range(4):
            new_grid[i].append(mat[i][4 - j - 1])
    return new_grid

def transpose(mat):
    new_grid = [[], [], [], []]
    for i in range(4):
        for j in range(4):
            new_grid[i].append(mat[j][i])
    return new_grid

def move_left(grid):
    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    return new_grid,changed

def move_right(grid):
    new_grid = reverse(grid)
    new_grid,changed1 = compress(new_grid)
    new_grid,changed2 = merge(new_grid)
    new_grid,temp = compress(new_grid)
    new_grid = reverse(new_grid)
    changed = changed1 or changed2
    return new_grid,changed

def move_up(grid):
    new_grid = transpose(grid)
    new_grid,changed1 = compress(new_grid)
    new_grid,changed2 = merge(new_grid)
    new_grid,temp = compress(new_grid)
    new_grid = transpose(new_grid)
    changed = changed1 or changed2
    return new_grid,changed

def move_down(grid):
    new_grid = transpose(grid)
    new_grid = reverse(new_grid)
    new_grid,changed1 = compress(new_grid)
    new_grid,changed2 = merge(new_grid)
    new_grid,temp = compress(new_grid)
    new_grid = reverse(new_grid)
    new_grid = transpose(new_grid)
    changed = changed1 or changed2
    return new_grid,changed