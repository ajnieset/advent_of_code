import re

def read_input():
    with open("input.csv", "r") as f:
        return "".join(f.readlines())

def solve():
    input_string = read_input()
    products = []

    # part 2
    dos = input_string.split("do()")
    valid_ops = "".join([do.split("don't()")[0] for do in dos])

    for match in re.findall(r"mul\((\d+),(\d+)\)", valid_ops):
        p = int(match[0]) * int(match[1])
        products.append(p)
    print(sum(products))

if __name__ == "__main__":
    solve()