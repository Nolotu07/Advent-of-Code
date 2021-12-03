#Nathan Olotu
#2021/12/01
#AoC 2021
#Problem Day 1 p2

lines = open('Day 1 input.txt','r').read().splitlines()

c, prev = 0, 99999

for i in range(2,len(lines)):
    total = int(lines[i]) + int(lines[i-1]) + int(lines[i-2])
    if total > prev:
        c+= 1
    prev = total

print(c)
