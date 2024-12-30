with open('input.txt', 'r') as f: #puts input into a 2D array with each index containing one step of the path
    grid = [[chr for chr in line.strip('\n')] for line in f.readlines()]
    f.close()
grid.append([' ' for _ in range(len(grid[0]))]) #adds an empty layer to the bottom to keep indexing in bounds

curp = [0, grid[0].index('|')] #starts in row 0 and finds the index with '|' indicating the starting path
direction = 'down' #always starts down
curpath = '|' #start will be '|' but will track '-', ' ', or letters
incs = {'down': [1,0], 'up': [-1,0], 'left': [0,-1], 'right':[0,1]} #how to move through grid to go 1 step in each direction
letters = '' #tracks letters seen for pt1
steps = 0 #counts steps for pt2
while True: #infinite loop
    curp = [curp[0] + incs[direction][0], curp[1] + incs[direction][1]] #increments the curp based on the direction
    curpath = grid[curp[0]][curp[1]] #updates the curpath sybol using curp
    steps += 1 #inc steps
    if curp[0] < 0 or curp[1] < 0 or curpath == ' ': break #breaks if the whole path has been traversed
    if curpath.isalpha(): letters += curpath #if the curpath symbol is a letter, it records that
    if curpath == '+': #if curpath is '+' the direction changes
        if direction == 'down' or direction == 'up': #if currently up/down new direction will be left/right
            if grid[curp[0]][curp[1]+1] == '-' or grid[curp[0]][curp[1]+1].isalpha() : direction= 'right' #looks right for a '-'
            elif grid[curp[0]][curp[1]-1] == '-' or grid[curp[0]][curp[1]-1].isalpha(): direction = 'left' #looks left for a '-'
        else: #if currently left/right, new direction will be up/down
            if grid[curp[0]+1][curp[1]] == '|' or grid[curp[0]+1][curp[1]].isalpha(): direction= 'down' #looks down for a '|'
            elif grid[curp[0]-1][curp[1]] == '|' or grid[curp[0]-1][curp[1]].isalpha(): direction = 'up' #looks up for a '|'
print(letters, 'steps:', steps)