with open('input.txt','r') as f:
    programs = [line.strip('\n').split(' ') for line in f.readlines()] #list of all programs with other info, for pt1
    all_prog = [prog[0] for prog in programs] #list of just programs
    prog_dict = {line[0]: [x.strip(',')  for x in line[3:]] for line in programs if len(line) > 2} #dict with name and branches
    weight_dict = {line[0]: int(line[1][1:-1]) for line in programs} #dict with name and weight
    keys = prog_dict.keys() #keys of any programs with branches
    f.close()
#pt 1
def pt1():
    held_discs = [] #discs that are being held by another disk, aka disks that are branches
    for p in programs: #goes through each program
        if len(p) > 2: #if disk has branch
            for prog in p[3:]: held_discs.append(prog.strip(',')) #the branches are appended since they are not the starting disk
    ans = list(set(all_prog)-set(held_discs))[0] #compares list of all branches to list of all programs and finds the one that is not common
    print(ans)#prints ans
    return(ans)#also returns ans

def sum_tower(prog): #starts wih starting branch and goes until it reaches program with no branches and works back to sum everything
    if prog in keys: #if program has branches
        sub_twr = prog_dict[prog] #creates list of the branches
        sums = [sum_tower(x) for x in sub_twr] #creates list of sums of each program branch using sum_tower
       # print('sums',sums, 'subtwr', sub_twr)
        if len(set(sums)) != 1: #all sums should be the same so if there is more than 1 value in the set, that's where the error occurs
            options = list(set(sums)) #options are a list of the 2 set values
            if sums.count(options[0]) == 1: #trying to find the value that is the wrong one
                odd = options[0] #odd one
                right = options[1] #correct one
            else: 
                odd = options[1]
                right = options[0]
            ind = sums.index(odd) #finds the index in the sums list where the odd one out is since this correlates to the sub_twr list as well
            w = sums[ind] - weight_dict[sub_twr[ind]] #the odd sum - the weight of the issue causing program
            a = right - w #the correct weight - the weight before the issue causing program is added = value that the issue causing program needs to be
            print('issue at',sub_twr[ind], 'weight w/o prob', w, 'ans',a) #only first statement matters
        return sum(sums) + weight_dict[prog]
    else: return weight_dict[prog] #program does not have branches, the total weight of it is just the weight of itself

ans = pt1()
sum_tower(ans)
