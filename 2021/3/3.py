with open("input.txt") as f: 
    values = f.readlines()

def part_1(): 
    length = len(values)
    result = [0] * len(values[0])
    for i in values: 
        print(i)
        for index, j in enumerate(i.strip()): 
            result[index] += int(j)
    print(result)
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

print(part_1())
