#from day 10
elements = 256
def run(loop_ct, input, my_list):
    skip_size, cur_ind = 0, 0 #initializing at 0
    for _ in range(loop_ct): #runs for specified amount of loops
        for length in input: #goes through each length in input
            rev = [my_list[k%elements] for k in range(cur_ind,cur_ind+length)][::-1] #reversed section based on length
            remaining = [my_list[k%elements] for k in range(cur_ind+length, cur_ind + elements)] #remaining unreversed parts
            a = rev + remaining #adds reversed part and unreversed part
            i = cur_ind #starts at current index
            for x in a: #goes through each number in the combined list
                my_list[i%elements] = x #puts the numbers in the correct index wrapping it around to the front if needed
                i+=1 #then increases the index
            cur_ind += length + skip_size #moves current index
            skip_size += 1 #inc skip size
    return my_list #returns list after all the transformations
def xor(my_list):
    dense_hash = [] #starts as empty list
    my_list = [str(my_list[i]) for i in range(len(my_list))] #converts each number to a string
    for i in range(0,len(my_list),16): #takes groups of 16 numbers
        x = '^'.join(my_list[i:i+16]) #creates a string joining each number by xor operator like 1^2^36^37^893 etc
        dense_hash.append(eval(x)) #evaluates that string using xor and appends it to dense hash
    #takes each number in dense hash and converts to hex in for 0x00 or 0x0 and removes the 0x at the start, if leftover is len 1, adds 0 at the start to make it 2 digits
    #then joins whole list to form a string and returns it
    hexadecimal = ''.join(['0'*(len(hex(dense_hash[i])[2:])%2) + hex(dense_hash[i])[2:] for i in range(len(dense_hash))])
    return hexadecimal
# key = 'amgozmfv'
key = 'amgozmfv'
def pt1():
    rounds, suffix, total_used, grid = 64, [17, 31, 73, 47, 23], 0, []
    for _ in range(128):
        string = key + '-' + str(_) #makes key 
        inp = [ord(string[i]) for i in range(len(string))] + suffix #creates the input list of instructions + suffix
        hexa = xor(run(rounds, inp, [i for i in range(elements)])) #same as day 10
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
# indices = [] #every index that is a used space
indices = [[r,c] for r in range(128) for c in range(128) if grid[r][c] == '1'] #list of indexs that are used (==1) in the grid
ct = 0 #initializes count at 0
ind_copy = indices.copy() #makes a copy since not using a copy messed things up a bit, this is just easier since my function checks if indexes are in the list anyway
for ind in indices: #goes through every index but is actually changing the index copy, i suspect the for loop was not updating how I thought using the non copy
    if ind in ind_copy: #checks if index is in the copy grid, if it's not it was unused or the group got deleted already and is accounted for
        ct += groups(ind, ind_copy) #deletes that group and increments ct which returns 1 when done running
print(ct)

