numbers = []
with open("puzzle_input.txt", "rb") as f:
    numbers = [int(i) for i in f.readlines()]


def sum(target):
    calculated = {}
    for num in numbers:
        diff = target - num
        if calculated.get(diff):
            return (diff, num)
        calculated[num] = diff


def sum_three():
    for num in numbers:
        target = 2020 - num
        sums = sum(target)
        if sums:
            x, y = sums
            return x * y * num


def get_multiple():
    x, y = sum(2020)
    return x * y


print(f"part 1 solution: {get_multiple()}")
print(f"part 2 solution: {sum_three()}")