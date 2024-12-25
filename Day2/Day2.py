with open('input.txt','r') as f:
    rows = [line.strip('\n').split('\t') for line in f.readlines()]
    f.close()
total1, total2 = 0, 0
for row in rows:
    r = [int(num) for num in row]
    total1 += max(r) - min(r)
    for num in r:
        for x in r:
            if x < num and num % x == 0: total2 += num//x
print(total1, total2)

