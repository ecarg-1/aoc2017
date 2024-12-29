steps = 349 #input amount of steps
buffer = [0] #initial buffer
def run(insertions, v): #takes in num of insertions and the number that we want to look at to see what is in the next index
    curp = 0 #current positions starts at 0
    for val in range(1, insertions + 1): #goes through each insertion with val being the number that will be inserted
        curp = (curp+steps) % len(buffer) + 1 #increments the curp by the steps from the input using mod to wrap around to the front, +1 since the insertion happens after that index
        buffer.insert(curp, val) #inserts the at the new curp
    print(buffer[buffer.index(v)+1]) #find the index of where val is, adds 1, and prints what is in that index

def pt2(insertions): #the index of 0 is always 0 regardless of what is inserted
    curp, len_buf, ans = 0, 1, 0 #does not create whole buffer, just tracks length, current position, and what is next to the 0th index
    for val in range(1, insertions + 1): #goes through each insertions
        curp = (curp+steps)%len_buf #finds the new curp using steps with mod to wrap 
        if curp == 0: ans = val #if the curp is 0, that value will be the index after 0
        curp, len_buf = curp + 1, len_buf + 1 #increments buffer length and also curp since the index is the inserted number
    print(ans)
#length of buffer is also equal to the value in the loop
run(2017, 2017) #pt1, wouldn't work for pt2 since it's too slow
pt2(50000000) #pt 2
