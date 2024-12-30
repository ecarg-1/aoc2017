with open('input.txt','r') as f:
    instructions = [line.strip('\n').split(' ') for line in f.readlines()]
    f.close()

def pt1():
    reg_dict = dict()
    last_freq, i = 0, 0
    while i<len(instructions): #iterates through instructions
        ins = instructions[i]
        if len(ins) == 3: 
            a = int(ins[1]) if ins[1].isnumeric() else ins[1]
            b = int(ins[2]) if ins[2].strip('-').isnumeric() else ins[2]
            if isinstance(b, str):
                if b not in reg_dict.keys(): reg_dict[b] = 0
        else: a = int(ins[1]) if ins[1].isnumeric() else ins[1]
        if isinstance(a, str):
                if a not in reg_dict.keys(): reg_dict[a] = 0
        match ins[0]:
            case 'snd': last_freq = a if isinstance(a, int) else reg_dict[a]
            case 'set': reg_dict[a] = b if isinstance(b, int) else reg_dict[b]
            case 'add': reg_dict[a] = reg_dict[a] + b if isinstance(b, int) else reg_dict[a] + reg_dict[b]
            case 'mul': reg_dict[a] = reg_dict[a] * b if isinstance(b, int) else reg_dict[a] * reg_dict[b]
            case 'mod': reg_dict[a] = reg_dict[a] % b if isinstance(b, int) else reg_dict[a] % reg_dict[b]
            case 'rcv': 
                x = reg_dict[a] if isinstance(a, int) else reg_dict[a]
                if x!=0: 
                    print('last played:', last_freq)
                    return 0
            case 'jgz': 
                x = a if isinstance(a, int) else reg_dict[a]
                y = b if isinstance(b, int) else reg_dict[b]
                if x > 0: i += y - 1
        i+=1

def pt2():
    cr = 0
    q =[[], []]
    reg_dict = [{'p':0}, {'p':1}]
    ind = [0,0]
    state = ['go','go']
    send_ct = 0
    while True:
        if state[0] == 'deadlock' and state[1] == 'deadlock': break
        ins = instructions[ind[cr]]
        if len(ins) == 3: 
            a = int(ins[1]) if ins[1].isnumeric() else ins[1]
            b = int(ins[2]) if ins[2].strip('-').isnumeric() else ins[2]
            if isinstance(b, str):
                if b not in reg_dict[cr].keys(): reg_dict[cr][b] = 0
        else: a = int(ins[1]) if ins[1].isnumeric() else ins[1]
        if isinstance(a, str):
                if a not in reg_dict[cr].keys(): reg_dict[cr][a] = 0
        match ins[0]:
            case 'snd': 
                q[(cr+1)%2].append(a) if isinstance(a, int) else q[(cr+1)%2].append(reg_dict[cr][a])
                if cr == 1: send_ct += 1
            case 'set': reg_dict[cr][a] = b if isinstance(b, int) else reg_dict[cr][b]
            case 'add': reg_dict[cr][a] = reg_dict[cr][a] + b if isinstance(b, int) else reg_dict[cr][a] + reg_dict[cr][b]
            case 'mul': reg_dict[cr][a] = reg_dict[cr][a] * b if isinstance(b, int) else reg_dict[cr][a] * reg_dict[cr][b]
            case 'mod': reg_dict[cr][a] = reg_dict[cr][a] % b if isinstance(b, int) else reg_dict[cr][a] % reg_dict[cr][b]
            case 'rcv': 
               if len(q[cr]) > 0: 
                   reg_dict[cr][a] = q[cr].pop(0)
                   state[cr] = 'go'
               else: 
                   if state[cr] == 'go': state[cr] = 'waiting'
                   else: state[cr] = 'deadlock'
                   cr = (cr+1)%2
                   ind[cr] -= 1
            case 'jgz': 
                x = a if isinstance(a, int) else reg_dict[cr][a]
                y = b if isinstance(b, int) else reg_dict[cr][b]
                if x > 0: ind[cr] += y - 1
        ind[cr] += 1
    print('Prog 1 sent',send_ct, 'times')

pt1()
pt2()
