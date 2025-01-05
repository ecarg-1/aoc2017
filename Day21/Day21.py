import numpy as np
import re, math
f, i= open('input.txt'), 0
pattern_guide, pattern_orientations = {}, []
for line in f.readlines():
    pattern_guide[i] = [0 if x == '.' else 1 for x in re.sub('/','',line.strip('\n').split()[-1])]      #dict where the key is the index in the follwihg list and the value is the new pattern
    x = np.array([0 if x == '.' else 1 for x in re.sub('/','',line.split()[0])])                        #flattened array of each input pattern
    shape = int(math.sqrt(len(x)))                                                                      #finds the dimensions of the matrix
    x = np.reshape(x, [shape, shape])                                                                   #this reshapes it into a 2D array instead of flat
    cur_orientations = []                                                                               #empty list to start all current orientations
    for _ in range(2):                                                                                  #loops twice (mirror, unmirrored)
        for _ in range(4):                                                                              #4 times for each 90 degree turn
            cur_orientations.append(list(x.flatten()))                                                  #appends the flattend version
            x = np.rot90(x)                                                                             #sets it equal to the 90 degree rotation so the rotations can continue upon each other
        x = np.fliplr(x)                                                                                #mirrors matrix
    pattern_orientations.append(cur_orientations)                                                       #appends list of orientations to patterns orientations list
    i+=1                                                                                                #increments to next index
f.close()                                                                                               #now we have a list of every orientation input and the we can use that index to match it to the output pattern
def make_grid(grid):                                        #divides the grid into 2x2 or 3x3 blocks and then matches the blocks                                                          
    num, blocks = 3, []                                     #sets num to 3 initially and makes block list 
    if len(grid) % 2 == 0: num = 2                          #sets num to 2 if needed
    for r in range(0,len(grid),num):                        #goes through each row 
        for c in range(0,len(grid),num):                    #an column based on num increments (2 or 3)
            blocks.append(grid[r:r+num, c:c+num].flatten()) #appends the flattened version to blocks
    matches = []                                            #blank list to hold the matches for the corresponding block
    for block in blocks:                                    #goes through each block
        i = 0                                               #stants indexing pattern orientations at 0
        while i < len(pattern_orientations):                #loops through pattern orientations
            if list(block) in pattern_orientations[i]:      #if matching pattern found in index i
                matches.append(pattern_guide[i])            #corresponding output is in dict with key i
            i+=1                                            #inc i
    shape = int(math.sqrt(len(matches)))                    #the matches are flattened so this is the shape (square) 
    match_shape = int(math.sqrt(len(matches[0])))           #shape of the match itself is also flat and needs to be shaped
    #creates a list of reshaped concatenated rows (added to the left) to later be all concatenated down
    reshaped_rows = [np.concatenate([np.reshape(matches[i], (match_shape, match_shape)) for i in range(x, x+shape)], axis=1) for x in range(0, len(matches),shape)]  
    final_reshaping = np.concatenate(reshaped_rows, axis=0) #concatenates all the pre concatenated rows 
    return final_reshaping                                  #returns final matrix
def run(loops):
    x = np.array([[0,1,0],[0,0,1],[1,1,1]])                 #start manually input as an np array
    for _ in range(loops): x = make_grid(x)                 #loops how ever many times
    print(np.count_nonzero(x))                              #prints # of non zeros/pixels that are on
run(5) #pt1
run(18) #pt2 (really slow)