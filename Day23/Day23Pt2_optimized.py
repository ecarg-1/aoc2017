import math
def prime(num):
    for div in range(2, math.floor(math.sqrt(num))):
        if num%div == 0: return False
    return True
h = 0
for b in range(108400, 125400 +1, 17): h = h + 1 if not prime(b) else h
print(h) #much faster, pretty much instant