with open('input.txt', 'r') as f:
    ins =  [line.strip('\n').split() for line in f.readlines()]
    f.close()
def run(part):
    registers, i, mul_ct = {chr(i): 0 for i in range(97,105)}, 0, 0
    if part == 2: registers['a'] = 1
    while i < len(ins):
        a = ins[i][1] if ins[i][1].isalpha() else int(ins[i][1])
        b = registers[ins[i][2]] if ins[i][2].isalpha() else int(ins[i][2])
        print( i, ins[i], ins[i][0], end=' ')
        match ins[i][0]:
            case 'set': 
                registers[a] = b
            case 'sub': registers[a] -= b
            case 'mul': 
                mul_ct += 1
                registers[a] *= b
            case 'jnz': 
                if isinstance(a, str): a = registers[a]
                if a != 0: i+=b-1
        print(registers, i)
        i += 1
    if part == 1: print(mul_ct)
    else: print(registers['h'])
run(2)