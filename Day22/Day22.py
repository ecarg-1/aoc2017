with open('input.txt') as f:
    grid = [line.strip('\n') for line in f.readlines()]
    f.close()
def run(loops, part=1):
    infected = {(r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '#'}
    curp, facing, move, inf_ct = (len(grid)//2, len(grid[0])//2), 0, {0: (-1,0), 1:(0,-1), 2:(1,0), 3: (0,1)}, 0
    weakened, flagged, clean = set(), set(), set()
    state_dict, d = {'infected': flagged, 'clean': weakened,'flagged':clean ,'weakened':infected}, {'infected':clean, 'clean':infected}
    if part == 2: d = state_dict
    for _ in range(loops):
        if curp in infected: 
            infected.remove(curp)
            d['infected'].add(curp)
            facing = (facing-1)%4
        elif curp in flagged: 
            flagged.remove(curp)
            d['flagged'].add(curp)
            facing = (facing+2)%4
        elif curp in weakened: 
            weakened.remove(curp)
            if part == 2: inf_ct += 1
            d['weakened'].add(curp)
        else: 
            d['clean'].add(curp)
            if part == 1: inf_ct += 1
            facing = (facing+1)%4
        curp = (curp[0] + move[facing][0], curp[1] + move[facing][1])
    print(inf_ct)
run(10000) #pt1
run(10000000 ,2) #pt2