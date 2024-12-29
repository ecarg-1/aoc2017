with open('input.txt', 'r') as f:
    dances = f.read().split(',')
    f.close()
programs = [chr(i) for i in range(97, 113)] #programs a-p
def dance(programs, loops): #takes in list of programs a-p and the amount of loops the dances should be done
    cpy, orders =programs.copy(), set() #for pt2, a copy of original a-p for recursion and a set of program orders
    for _ in range(loops): #loops how ever many times
        for d in dances: #goes through each dance step
            match d[0]: #does the corresponding edits
                case 's': #spin
                    num = int(d[1:])
                    programs = programs[-num:] + programs[:-num]
                case 'x': #swap ind
                    a, b = d[1:].split('/')
                    programs[int(a)], programs[int(b)] = programs[int(b)], programs[int(a)]
                case 'p': #swap prog
                    a, b = d[1:].split('/')
                    for i in range(len(programs)):
                        if programs[i]==a: programs[i]=b
                        elif programs[i] ==b: programs[i]=a
        if ''.join(programs) not in orders: orders.add(''.join(programs)) #adds unseen program order to set
        else: return dance(cpy, loops%_) #if order has been seen, it repeats and only needs to be done loops%repeats times so it runs 1 more loop and returns it
    return ''.join(programs) #if no repetitions, just returns it
print(dance(programs.copy(), 1)) #pt 1
print(dance(programs.copy(), 1000000000)) #pt2


