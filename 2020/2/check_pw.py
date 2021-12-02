from collections import namedtuple

Password = namedtuple("Password", ["mini", "maxi", "target", "pw"])


def get_lines():
    lines = []
    with open("puzzle_input.txt", "rb") as pws:
        lines = pws.read().splitlines()
    return lines


def clean_line(line):
    line = line.decode("utf-8")
    params = line.split(" ")
    occurences = params.pop(0).split("-")
    min_occur = int(occurences[0])
    max_occur = int(occurences[1])
    letter = params.pop(0).strip(":")
    pw = params.pop(0)
    return Password(mini=min_occur, maxi=max_occur, target=letter, pw=pw)


def get_valid_pw_within_range():
    valid_pw_count = 0
    for line in get_lines():
        args = clean_line(line)
        count = args.pw.count(args.target)
        valid_pw_count += count >= args.mini and count <= args.maxi
    return valid_pw_count


def get_valid_pw_by_index():
    valid_pw_count = 0
    for line in get_lines():
        args = clean_line(line)
        first_index = args.pw[args.mini - 1]
        second_index = args.pw[args.maxi - 1]
        valid_pw_count += (first_index == args.target) != (second_index == args.target)
    return valid_pw_count


print(f"this is the valid count: {get_valid_pw_within_range()}")
print(f"this is the valid count: {get_valid_pw_by_index()}")
