#Nathan Olotu
#2021/12/01
#AoC 2021
#Problem Day 1 p1

lines = open('Day 1 input.txt','r').read().splitlines()

count = 0
lastnum = 162


for line in lines:
    line = int(line)
    if line > lastnum:
        count += 1
    lastnum = line


print(count)

