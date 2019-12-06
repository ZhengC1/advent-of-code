import math
data = []
with open('test_input.txt') as file: 
    data = file.readlines()

answer = sum([(math.floor(int(i)/3) - 2) for i in data])

print(F"This is the answer to part one {answer}")

def get_fuel(number):
    result = math.floor(number/3) - 2
    if result <= 0:
        return 0
    return result + get_fuel(result)

result = 0
for module in data:
    result += get_fuel(int(module))

print(F"answer for part 2 {result}")


