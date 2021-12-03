#Nathan Olotu
#2021/12/03
#AoC 2021
#Problem Day 3 p1



with open('Day 3 input.txt') as input_file:
    input_array = [list(line.rstrip()) for line in input_file]
    input_array = str(input_array)

for i in input_array:
    list_of_words = input_array
    frequency_distribution = FreqDist(list_of_words) 
    print(frequency_distribution)
    most_common_element = frequency_distribution.max()
    print (most_common_element)
