<<<<<<< HEAD
from collections import Counter
from functools import reduce
import operator

def compute_checksum():
    data = []
    with open('input.txt', 'r') as f:
        data = f.readlines()

    numbers = []
    for line in data:
        count = set(Counter(line).values())
        if 1 in count:
            count.remove(1)
        numbers.append(count)
    nums = {}
    for count in numbers:
        for i in count:
            if i in nums.keys():
                nums[i] = nums[i] + 1
            else: 
                nums[i] = 1
    print(reduce(operator.mul, nums.values()))


compute_checksum()
=======
data = []
with open('input.txt', 'r') as f:
    data = f.readlines()



>>>>>>> c49fd9ada18463e67d1b1d30b74871efe0127ff0
