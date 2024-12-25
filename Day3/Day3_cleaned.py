def find_ring(goal): #finds the ring around the goal
    incs, nums = [1, 3, 5, 7], [1, 1, 1, 1] # right, up, left, down
    ind, exceeded_goal = 0, False #index of how far ring goes out
    while not exceeded_goal: #goal is exceeded once any of the nums become greater than goal
        nums = [nums[i] + incs[i] for i in range(4)] #incs nums by inc
        incs = [incs[i] + 8 for i in range(4)] #incs incs by 8
        ind += 1 #incs ind by 1
        for num in nums: exceeded_goal = True if num > goal else exceeded_goal #goal is guaranteed to be below these 4 numbers 
    return ind, nums #returns ind (radius of ring) and numbers
def run_pt1(goal):
    ind, ring = find_ring(goal)
    if goal in ring: return ind #if goal is in the ring, it's the index away from the center
    if goal < ring[0]: ring_num, difference = ring[0], 1
    elif goal < ring[1]: ring_num, difference = ring[1], 0
    elif goal < ring[2]: ring_num, difference = ring[2], 0
    elif goal < ring[3]: ring_num, difference = ring[3], 0
    while ring_num - difference != goal: difference += 1
    if difference <= ind: return ind + difference
    else: return ind - difference 
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
    inc = 2 #how much to increment in each direction when spiraling
    while True: #each loop starts with cur_pos (x,x) and finishes with cur_pos (x+1, x+1)
        spiral = expand(spiral) #once spiral is expanded, the new cur_pos is (x+2, x+2) hence why inc increases by 2 each loop 
        cur_pos = [inc, inc + 1] #moves right once from current position (inc,inc)
        spiral[cur_pos[0]][cur_pos[1]] = sum_ind(cur_pos, spiral) #sums surroundings and puts it in the current position
        if sum_ind(cur_pos, spiral) > goal: return sum_ind(cur_pos, spiral) #checks if the number is greater than the goal
        xy = [[-1, 0, 0], [0,-1, 1],[1, 0, 1],[0, 1, 1]] #cur pos[0] inc, cur pos[1] inc, for loop inclusive or not
        for z in xy:
            for _ in range(1, inc + z[2]):
                cur_pos = [cur_pos[0] + z[0], cur_pos[1] + z[1]]
                spiral[cur_pos[0]][cur_pos[1]] = sum_ind(cur_pos, spiral)
                if sum_ind(cur_pos, spiral) > goal: return sum_ind(cur_pos, spiral)
        inc += 2
puzzle_input = 368078
print(run_pt1(puzzle_input)) #part 1
print(run_pt2(puzzle_input)) #part 2

     
