a, b = 883, 879

def gen(a, b, pairs, part=1):
    ct = 0
    for _ in range(pairs):
        a, b = (a*16807)%2147483647, (b*48271)%2147483647
        if part == 2:
            while a%4 != 0 : a = (a*16807)%2147483647
            while b%8 != 0 : b = (b*48271)%2147483647
        abin, bbin = bin(a)[-16:], bin(b)[-16:]
        if abin == bbin: ct += 1
    return ct

pairs1, pairs2 = 40000000, 5000000
print(gen(a, b, pairs1)) #pt 1
print(gen(a, b, pairs2, part=2)) #pt 2