f = open('input.txt','r')
conn = [[int(l[i]) for i in range(len(l))]for l in [line.strip('\n').split('/') for line in f.readlines()]]
f.close()
def run(cur_order = [], last_comm = 0, original=True, result = []):                                         #takes in order of links, last common number, bool of original loop, results
    if original: possibilities = [c for c in conn if c.count(0) !=0]                                        #if it is the first loop, finds any connectors with 0 to start 
    else: possibilities = [c for c in conn if c.count(last_comm) !=0 and c not in cur_order]                #if not, it finds any connectors that have a common number with the previous connector
    if len(possibilities) == 0 : result.append([sum([sum(c) for c in cur_order]), len(cur_order)])          #appends (strength, length) for each finished bridge
    for p in possibilities:                                                                                 #iterates through possibilities
        cpy, lc = cur_order.copy(), p[0] if p[0] != last_comm else p[1]                                     #makes a copy of the current order and determines the new last commonality between the possibility and the previous link
        cpy.append(p)                                                                                       #appends possibility to current order
        run(cpy, lc, False, result)                                                                         #runs the same function again to find new possibilites
    if original:                                                                                            #prints results if finished the original loop
        maxl = max([r[1] for r in result])                                                                  #precalculated max length for speed
        return print(max([r[0] for r in result]), max([s[0] for s in [r for r in result if r[1] == maxl]])) #returns max strength and max strength of longest link                                                   #the original loop will return the max strength
run()