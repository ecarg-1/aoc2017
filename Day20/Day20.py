import re
with open('input.txt','r') as f:
    particles = [[[int(p[i]) for i in range(x,x+3)] for x in range(0,7,3)] for p in [re.findall(r'\d{1,6}|-\d{1,6}', line) for line in f.readlines()]]
    f.close()
mina = 10000
for i in range(len(particles)):
    md = sum([abs(x) for x in particles[i][2]])
    if mina > md: 
        mina = md
ind = []
for i in range(len(particles)):
    b = sum([abs(x) for x in particles[i][2]])
    if b == mina: ind.append(i)
minv = 10000
minv_ind = 0
for y in ind:
    c = sum([abs(x) for x in particles[y][1]])
    if minv > c:
        minv = c
        minv_ind = y
print(minv_ind) #pt 1

status = [True for _ in range(len(particles))]
def simulate():
    for i in range(len(particles)):
        if status[i] == True:
            for j in range(3): particles[i][1][j] += particles[i][2][j]
            for k in range(3): particles[i][0][k] += particles[i][1][k]
def remove_collisions():
    positions = [particles[i][0] for i in range(len(particles)) if status[i] == True]
    for i in range(len(particles)):
        if positions.count(particles[i][0]) > 1: status[i] = False
for _ in range(100): 
    simulate()
    remove_collisions()
print(status.count(True)) #pt2

