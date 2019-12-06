from itertools import accumulate, cycle
read_data = []
with open('input.txt', 'r') as f:
    read_data = f.readlines()


converted = map(int, read_data)
visited = set()

print(next(i for i in accumulate(cycle(converted)) if i in visited or visited.add(i)))
