with open('input.txt','r') as f:
    ins_list = [line.strip('\n').split(' ') for line in f.readlines()]
    f.close()

reg_dict, max_val = dict(), 0
for ins in ins_list:
    if ins[-3] not in reg_dict.keys(): reg_dict[ins[-3]] = 0 #sets conditional register to 0 if not already seen in instructions
    if ins[0] not in reg_dict.keys(): reg_dict[ins[0]] = 0 #register to be modified to 0 if not already seen in instructions
    cond_statement = ''.join([str(reg_dict[ins[-3]])]+ins[-2:]) #makes a conditional statement in string form ex: 123 != 39
    if eval(cond_statement): #evaluates the conditional string as if it were integers returning True or False
        match ins[1]: #inc or dec
            case 'dec': reg_dict[ins[0]] -= int(ins[2]) 
            case 'inc': reg_dict[ins[0]] += int(ins[2])
        max_val = max(max_val, reg_dict[ins[0]])
print(max(reg_dict.values()), max_val)
