with open('input.txt', 'r') as f:
    pipes = {int(line.strip('\n').split(' ')[0]): [int(line.strip('\n').split(' ')[i].strip(',')) for i in range(2, len(line.strip('\n').split(' ')))] for line in f.readlines()}
    f.close()

def find_pipes(prog, pipeset, original=True): #takes in a pipe number
    con_progs = pipes[prog] #creates a list of pipes connected
    if prog not in pipeset: pipeset.add(prog) #if the input pipe is not in the pipeset, it adds it
    else: return None #if it is, it's already accounted for and just returns None as a way to break out of the function during recursion
    for p in con_progs: find_pipes(p, pipeset, False) #for each pipe that connects, it runs find_pipes again which adds any new connected pipes to the set
    if original: return pipeset #if it's the first function called, it's stopped recursing and returns pipeset (used in pt 2 otherwise would've just returned length)
def pt2():
    ct, groupset = 0, set()
    for p in pipes.keys(): #goes through each pipe
        if p not in groupset: #if it is not in groupset
            groupset = groupset.union(find_pipes(p, set())) #it adds that pipe and every connected pipe to groupset
            ct+=1 #increments the count which will only happen when a non accounted for number is found
    return ct

print(len(find_pipes(0, set()))) #pt 1
print(pt2()) #pt 2