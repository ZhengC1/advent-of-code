import math
data = []
with open('test_input.txt') as file: 
    data = file.readlines()

answer = sum([(math.floor(int(i)/3) - 2) for i in data])

print(answer)

