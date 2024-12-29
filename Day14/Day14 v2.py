from Day10 import get_hex
key = 'amgozmfv'
def pt1():
    total_used, grid = 0, []
    for _ in range(128):
        string = key + '-' + str(_) #makes key 
        hexa = get_hex(string) #gets hex from Day 10
        binary = ''.join(['0'*((4-len(bin(int(hexa[i], 16))[2:]))%4) + bin(int(hexa[i], 16))[2:] for i in range(len(hexa))]) #makes binary string adding 0's before if there are not already 4 digits
        total_used += binary.count('1') #counts number of 1's
        grid.append([binary[i] for i in range(len(binary))]) #also makes a grid for pt2
    print('Part 1:',total_used) #prints out for pt1
    return grid #returns grid to be used in pt 2

def groups(ind, indices): #removes an entire group of touching used spaces
    indices.remove(ind) #first removes the index specified
    options = [[1,0],[-1,0],[0,1],[0,-1]] #options for squares adjacent
    for o in options: #goes through options
        if [ind[0] + o[0], ind[1] + o[1]] in indices: groups([ind[0] + o[0], ind[1] + o[1]], indices) #it uses recursion to check the surounding cells for that index to remove the whole group
    return 1
    
grid = pt1() #pt 1 and starting pt2
indices = [[r,c] for r in range(128) for c in range(128) if grid[r][c] == '1'] #list of indexs that are used (==1) in the grid
ct = 0 #initializes count at 0
ind_copy = indices.copy() #makes a copy since not using a copy messed things up a bit, this is just easier since my function checks if indexes are in the list anyway
for ind in indices: #goes through every index but is actually changing the index copy, i suspect the for loop was not updating how I thought using the non copy
    if ind in ind_copy: #checks if index is in the copy grid, if it's not it was unused or the group got deleted already and is accounted for
        ct += groups(ind, ind_copy) #deletes that group and increments ct which returns 1 when done running
print(ct)

