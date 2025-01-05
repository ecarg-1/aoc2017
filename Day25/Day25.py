f = open('input.txt','r')
lines = [line.strip('\n')[:-1].split() for line in f.readlines()]
f.close()
state_dict = {lines[i][-1]:[int(lines[i+j][-1]) if lines[i+j][-1].isnumeric() else lines[i+j][-1] for j in range(1,9)] for i in range(len(lines)) if lines[i] and lines[i][0] == 'In'} #list comp within conditional dict comp 
steps = int(lines[1][-2])
cur_state, curp, ones = lines[0][-1], 0, set()
for _ in range(steps):
    ind = 4 if curp in ones else 0                                              #if curp=1, starts at index 4 else it starts at 0 but the data is the same relative distance from the start for each
    if state_dict[cur_state][ind+1] == 1: ones.add(curp)                        #if the number should be set to 1, it is added to curp (duplicates don't matter since it's a set)
    else: ones.discard(curp)                                                    #if it's set to 0, it discarded which won't throw an error if it was already 0 (not in the set to begin with)
    curp = curp + 1 if state_dict[cur_state][ind+2] == 'right' else curp - 1    #inc or dec curp according to left (dec) or right (inc)  
    cur_state = state_dict[cur_state][ind+3]                                    #sets next state
print(len(ones))                                                                #prints total amount of ones