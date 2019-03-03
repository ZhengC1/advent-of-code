read_data = []
with open('input.txt', 'r') as f:
    read_data = f.readlines()

print(sum(map(int, read_data)))

