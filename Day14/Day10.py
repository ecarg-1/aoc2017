elements = 256
pt1_in = [76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229]
def run(loop_ct, input, my_list):
    skip_size, cur_ind = 0, 0 #initializing at 0
    for _ in range(loop_ct): #runs for specified amount of loops
        for length in input: #goes through each length in input
            rev = [my_list[k%elements] for k in range(cur_ind,cur_ind+length)][::-1] #reversed section based on length
            remaining = [my_list[k%elements] for k in range(cur_ind+length, cur_ind + elements)] #remaining unreversed parts
            a = rev + remaining #adds reversed part and unreversed part
            i = cur_ind #starts at current index
            for x in a: #goes through each number in the combined list
                my_list[i%elements] = x #puts the numbers in the correct index wrapping it around to the front if needed
                i+=1 #then increases the index
            cur_ind += length + skip_size #moves current index
            skip_size += 1 #inc skip size
    return my_list #returns list after all the transformations
def xor(my_list):
    dense_hash = [] #starts as empty list
    my_list = [str(my_list[i]) for i in range(len(my_list))] #converts each number to a string
    for i in range(0,len(my_list),16): #takes groups of 16 numbers
        x = '^'.join(my_list[i:i+16]) #creates a string joining each number by xor operator like 1^2^36^37^893 etc
        dense_hash.append(eval(x)) #evaluates that string using xor and appends it to dense hash
    #takes each number in dense hash and converts to hex in for 0x00 or 0x0 and removes the 0x at the start, if leftover is len 1, adds 0 at the start to make it 2 digits
    #then joins whole list to form a string and returns it
    hexadecimal = ''.join(['0'*(len(hex(dense_hash[i])[2:])%2) + hex(dense_hash[i])[2:] for i in range(len(dense_hash))])
    return hexadecimal
def get_hex(string): #added this for Day 14
    rounds, suffix = 64, [17, 31, 73, 47, 23]
    string = [ord(string[i]) for i in range(len(string))] + suffix
    b = run(rounds, string, [i for i in range(elements)])
    return xor(b)
