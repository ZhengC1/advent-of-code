def get_tree_map():
    lines = []
    with open("puzzle_input.txt", "rb") as pws:
        lines = pws.read().splitlines()
    return [line.decode("utf-8") for line in lines]


def calculate_tree_obstacles(x, b):
    x_index = 0
    b_index = 0
    tree_count = 0
    tree_map = get_tree_map()
    while b_index < len(tree_map):
        location = tree_map[b_index][x_index]
        x_index = (x_index + x) % len(tree_map[b_index])
        b_index += b
        tree_count += location == "#"
    return tree_count

print(f"this is the tree count: {calculate_tree_obstacles(3, 1)}")

"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""

combined = (
    calculate_tree_obstacles(1, 1)
    * calculate_tree_obstacles(3, 1)
    * calculate_tree_obstacles(5, 1)
    * calculate_tree_obstacles(7, 1)
    * calculate_tree_obstacles(1, 2)
)
print(f"this if the combined tree count {combined}")
