with open("input.txt") as f: 
    values = f.readlines()

def part_1():
    horizontal = 0
    depth = 0
    for steps in values: 
        direction, num = steps.split()
        num = int(num)
        if direction == "forward":
            horizontal += num
        else: 
            if direction == "down":
                depth += num
            else:
                depth -= num

    print(horizontal * depth)

def part_2():
    horizontal = 0
    depth = 0
    aim = 0
    for steps in values: 
        direction, num = steps.split()
        num = int(num)
        if direction == "forward":
            horizontal += num
            depth += aim * num
        else: 
            if direction == "down":
                aim += num
            else:
                aim -= num

    print(horizontal * depth)


part_2()
