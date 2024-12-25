with open('input.txt','r') as f:
    string = f.read()
    f.close()
total = 0
if string[-1] == string[0]: total += int(string[0])
for i in range(len(string)-1):
    if string[i] == string [i+1]: total += int(string[i])
print(total) # part 1

total = 0
for i in range(len(string)):
    if string[i] == string[(i+len(string)//2)%len(string)]:
        total += int(string[i])
print(total) #part 2