#Nathan Olotu
#2021/12/02
#AoC 2021
#Problem Day 2 p1



with open('Day 2 input.txt') as input_file:
    input_array = [line.split() for line in input_file]


pos = 0
depth = 0


for i in input_array:
    if i[0] == "forward":
        pos += int(i[1])
    elif i[0] == "down":
        depth += int(i[1])
    elif i[0] == "up":
        depth -= int(i[1])


print("Result: ", pos*depth)
