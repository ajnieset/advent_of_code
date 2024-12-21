from scipy.ndimage import rotate
import numpy as np

def get_input():
    with open("test_input.csv", "r") as f:
        return f.readlines()
    
def count_xmas(l: list[list[str]]):
    count = 0
    for line in l:
        count += line.count("XMAS")
    return count

    
def solve():
    xmas_count = 0
    lines = get_input()

    original = list(map(lambda x: "".join(x), [list(line.strip("\n")) for line in lines]))

    xmas_count += count_xmas(original)

    rotated = list(map(lambda x: "".join(x), zip(*original[::-1])))

    xmas_count += count_xmas(rotated)

    print(xmas_count)

def check_xmas(c: str):
    pass

def solve2():
    xmas_count = 0
    lines = get_input()

    original = [list(line.strip("\n")) for line in lines]

    for line in original:
        for char in line:
            xmas, count = check_xmas(char)
            if xmas:
                xmas_count += count

if __name__ == "__main__":
    solve()
    solve2()