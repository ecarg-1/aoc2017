with open('input.txt','r') as f:
    moves = f.read().split(',')
    f.close()
incs = {'n': [2,0], 'ne': [1,1], 'nw': [1,-1], 's': [-2,0], 'se': [-1, 1], 'sw': [-1, -1]}
def distance(r, c):
    if abs(r) >= abs(c):
        return abs(abs(r)-abs(c))//2 + abs(c)
    ct, direction = 0, ''
    if r >= 0 and c > 0: direction = 'nw' 
    elif r >= 0 and c < 0: direction = 'ne' 
    elif r < 0 and c < 0: direction = 'se' 
    else: direction = 'sw' 
    while abs(r) != abs (c): r, c, ct = r+incs[direction][0], c+incs[direction][1], ct+1
    return ct + abs(r)
def run():
    loc, farthest = [0, 0], 0
    for m in moves:
        loc[0], loc[1] = loc[0] + incs[m][0], loc[1] + incs[m][1]
        farthest = max(farthest, distance(loc[0], loc[1]))
    return distance(loc[0],loc[1]), farthest

print(run())