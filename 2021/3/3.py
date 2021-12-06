import math
from functools import reduce
def get_values(input_file):
    with open(input_file) as f: 
        return [v.strip() for v in f]

def part_1(values): 
    length = len(values)
    result = [0] * len(values[0])
    print(len(values))
    for i in values: 
        for index, j in enumerate(i.strip()): 
            result[index] += int(j)
    min_num = ""
    max_num = "" 
    for i in result: 
         if i > 500: 
             max_num += "1"
             min_num += "0"
         else: 
             min_num += "1"
             max_num += "0"
    return int(max_num, 2) * int(min_num, 2)

def get_bit_avg(values, index):
    return math.ceil((reduce(lambda x, y: x + y, [int(i[index]) for i in values]) / len(values)) * 100)

def part_2(values): 
    co2_values = values
    oxy_values = values
    for index in range(len(values[0])): 
        if len(co2_values) > 1:
            curr_bit = get_bit_avg(co2_values, index)
            co2_bit = curr_bit >= 50 
            co2_values = [i for i in co2_values if int(i[index]) != co2_bit] 
        if len(oxy_values) > 1:
            curr_bit = get_bit_avg(oxy_values, index)
            oxy_bit = curr_bit >= 50 
            oxy_values = [i for i in oxy_values if int(i[index]) == oxy_bit]
    co2 = int("".join(i for i in co2_values), 2)
    oxy = int("".join(i for i in oxy_values), 2) 
    return co2 * oxy

values = get_values("input.txt")
print(part_2(values))

