with open('input.txt', 'r') as f:
    pw_list = [line.strip('\n').split(' ') for line in f.readlines()]
    f.close()
total1, total2 = 0, 0 
for words in pw_list:
    if len(set(words)) == len(words): total1 += 1 #set removes dupes, if lengths are same, no dupes and valid
    words = [''.join(sorted(word)) for word in words] #alphabetizes each word, removes dupes, if lenth is same, no dupes and valid
    if len(set(words)) == len(words): total2 += 1
print(total1, total2) #part1, part2