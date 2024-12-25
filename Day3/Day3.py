puzzle_input = 368078
def find_ring(goal): #finds the ring around the goal
    incs, nums = [1, 3, 5, 7], [1, 1, 1, 1] # right, up, left, down
    ind, exceeded_goal = 0, False #index of how far ring goes out
    while not exceeded_goal: #goal is exceeded once any of the nums become greater than goal
        nums = [nums[i] + incs[i] for i in range(4)] #incs nums by inc
        incs = [incs[i] + 8 for i in range(4)] #incs incs by 8
        ind += 1 #incs ind by 1
        for num in nums:  
            if num > goal: exceeded_goal = True #goal is guaranteed to be below these 4 numbers 
    return ind, nums #returns ind (radius of ring) and numbers
def run(goal):
    ind, ring = find_ring(goal)
    if goal in ring: return ind #if goal is in the ring, it's the index away from the center
    if goal < ring[0]: #if goal is less than the first number
        difference = 0 
        while ring[0] - difference != goal: difference += 1 #find how far away it is
        if difference <= ind-1: return ind + difference #returns based on difference
        else: return 2 * ind - 1 - (difference - (ind-1)) 
    elif goal < ring[1] or goal < ring[2]: #ring[1] and ring[2] same pattern
        difference = 0
        if goal < ring[1]:
            while ring[1] - difference != goal: difference += 1
        else:
            while ring[2] - difference != goal: difference += 1
        if difference <= ind: return ind + difference
        else: return 2 * ind - (difference - ind)
    elif goal < ring[3]:
        difference = 0
        while ring[3] - difference != goal: difference += 1
        if difference <= ind: return ind + difference 
        else: return 2 * ind - (difference - ind)

def expand(spiral):
    len_nr = len(spiral) + 2
    empty_row, new_spiral = [], []
    for _ in range(len_nr): empty_row.append(0)
    new_spiral.append(empty_row)
    for i in range(len(spiral)): new_spiral.append([0] + spiral[i] + [0])
    new_spiral.append(empty_row.copy())
    return new_spiral

def sum_ind(cur_pos, spiral):
    return sum(spiral[cur_pos[0] - 1][cur_pos[1]-1:cur_pos[1]+2] + spiral[cur_pos[0] + 1][cur_pos[1]-1:cur_pos[1]+2] + spiral[cur_pos[0]][cur_pos[1]-1:cur_pos[1]+2:2])

def run_pt2(goal):
    spiral = [[0,0,0],[0,1,0],[0,0,0]]
    rad = 2
    inc = 2
    for x in spiral: print(x)
    print()
    for p in range(3):
        cur_pos = [rad,rad]
        print('cur_p', cur_pos)
        #step 0 expand
        spiral = expand(spiral)
        #step 1 move right once from current position
        cur_pos = [cur_pos[0], cur_pos[1] + 1]
        # print('cur_p', cur_pos)

        spiral[cur_pos[0]][cur_pos[1]] = sum_ind(cur_pos, spiral)
        if sum_ind(cur_pos, spiral) > goal: return sum_ind(cur_pos, spiral)
        for x in spiral: print(x)
        print()
        #step 2 move up u_inc times
        for _ in range(1, inc):
            cur_pos = [cur_pos[0] - 1, cur_pos[1]]
            spiral[cur_pos[0]][cur_pos[1]] = sum_ind(cur_pos, spiral)
            if sum_ind(cur_pos, spiral) > goal: return sum_ind(cur_pos, spiral)
        for x in spiral: print(x)
        print()
        #step 3 move left l_inc times
        for _ in range(1, inc + 1):
            cur_pos = [cur_pos[0], cur_pos[1] - 1]
            spiral[cur_pos[0]][cur_pos[1]] = sum_ind(cur_pos, spiral)
            if sum_ind(cur_pos, spiral) > goal: return sum_ind(cur_pos, spiral)
        for x in spiral: print(x)
        print()
        #step 4 move down d_inc times
        for _ in range(1, inc + 1):
            cur_pos = [cur_pos[0] + 1, cur_pos[1]]
            spiral[cur_pos[0]][cur_pos[1]] = sum_ind(cur_pos, spiral)
            if sum_ind(cur_pos, spiral) > goal: return sum_ind(cur_pos, spiral)
        for x in spiral: print(x)
        print()
        #step 5 move right r_inc times
        for _ in range(1, inc + 1):
            cur_pos = [cur_pos[0], cur_pos[1] + 1]
            spiral[cur_pos[0]][cur_pos[1]] = sum_ind(cur_pos, spiral)
            if sum_ind(cur_pos, spiral) > goal: return sum_ind(cur_pos, spiral)
        inc += 2
        for x in spiral: print(x)
        rad += 2
        print('curpos', cur_pos)
        print()



#print(run(puzzle_input))
print(run_pt2(puzzle_input))