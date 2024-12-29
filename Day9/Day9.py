with open('input.txt','r') as f:
    string = f.read()
    f.close()
i, within_garbage, open_groups, score, garbabge_ct = 0, False, 0, 0, 0
while i < len(string):
    if not within_garbage: #if we are not in a garbage string
        match string[i]:
            case '{': open_groups += 1 #{ means opening of a group
            case '}': 
                score += open_groups #a group is closed and score=open groups
                open_groups -= 1 #since group becomes closed, open groups decrement
            case '<': within_garbage = True #< means start of a trash string
    else: #we are in a garbage string
        match string[i]:
            case '!': i+=1 #means to ignore the next character, index increments
            case '>': within_garbage = False #ends trash string
            case _: garbabge_ct += 1 #if not ! or > then it is a garbage character that adds to the count for pt2
    i+=1
print('score:',score,'\ngarbage count:',garbabge_ct)