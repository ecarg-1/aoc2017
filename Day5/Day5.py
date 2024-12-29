with open('input.txt','r') as f:
    jumps = [int(line) for line in f.readlines()]
    f.close()
def run(part1=True):
    cur_ind, steps = 0, 0
    while cur_ind < len(jumps):
        prev_ind = cur_ind
        cur_ind += jumps[cur_ind]
        if part1: jumps[prev_ind] += 1
        else:
            if jumps[prev_ind] >= 3: jumps[prev_ind] -= 1
            elif jumps[prev_ind] <= -3: jumps[prev_ind] += 1
            else: jumps[prev_ind] += 1
        steps += 1
    return steps
print(run()) #part1
print(run(False))#part2