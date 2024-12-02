from collections import Counter

def read_input() -> list:
    with open("input.csv", 'r') as f:
        return [ x.strip("\n").split("   ") for x in f.readlines()]
    
def solve():
    data = read_input()

    first, second = list(zip(*data))

    print(sum(map(lambda x: abs(int(x[0]) - int(x[1])), zip(sorted(first), sorted(second)))))

    counted = Counter(second)

    total = 0
    for item in first:
        if item in counted:
            total += int(item) * counted[item]

    print(f"{total = }")

    
if __name__ == "__main__":
    solve()