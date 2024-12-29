with open('input.txt','r') as f:
    layers = {int(line.strip('\n').split(' ')[0][:-1]): int(line.strip('\n').split(' ')[-1]) for line in f.readlines()}
    f.close()

def locate(picos, r, pos): #follows a triangle wave 
    for x in range(picos + 1): 
        pos = -(abs((x % ((r - 1) * 2)) - (r - 1)) - (r - 1)) 
    return pos

def valid_delays(d ,r, start ,end): #set of valid delays from start to end
    x = (r-2)*2+2 #derived these equataions from patterns
    ok_t = set()
    for t in range(start, end + 1):
        if ((t%x)+d)%x != 0: ok_t.add(t) #basically if this equation = 0, it's not valid otherwise it adds it to the set
    return ok_t #returns the set

def pt2(): #made this because brute force was not fast enough, somehow this worked much quicker although still slow
    jump = 1000000 #kind of unknown so doing largeish intervals
    start, end = 0, jump #initial range
    while True:
        my_set = valid_delays(0,3 ,start,end) #initializes the set with the first thing in dict so there's something to intersect with(hard coded here but doesn't have to be)
        for d, r in layers.items(): #goes through each layer 
            my_set = my_set.intersection(valid_delays(d, r, start, end)) #finds valid delays and intersects it with the existing set leaving valid delays for both
        if len(my_set) > 0: break #if at the end of all the intersections, there is at least 1 common one, the answer is contained in the set
        start, end = end, end + jump #if no commonalities, the range is incremented
    return min(list(my_set)) #returns the minimum value of the set where the answer is contained

print(sum([t*layers[t] for t in range(max(layers.keys()) + 1) if t in layers.keys() and locate(t,layers[t],0) == 0])) #pt 1
print(pt2()) #pt2