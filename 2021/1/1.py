import math
def get_values():
    with open("input.txt") as f: 
        values = f.readlines()
    return [int(i) for i in values]


def part_1(values):
    result = -1 
    prev = -math.inf
    for i in values: 
        if int(i) > prev:
            result += 1
        prev = int(i)

    print(result)

def part_2(values):
    result = -1
    prev = -math.inf
    length = len(values)
    for i in range(len(values)):
        comp = 0
        if (i + 2  < length): 
            comp += values[i] + values[i + 1] + values[i + 2]
        else: 
            break
        if comp > prev:
            result += 1
        prev = comp
    print(result)

part_2(get_values())

