b_init, c, h = 108400, 125400, 0
for b in range(b_init, c + 1, 17):
    f = 1
    for d in range(2, b):
        if b%d != 0: continue       #skips numbers that are not factors of b to speed it up
        for e in range(2, b):
            if b%e != 0: continue   #skips numbers that are not factors of b to speed it up
            if d*e == b: f = 0
    if f==0: h+=1
print(h) #faster than using pt1 code but still took a long time