from solution import solve as part_1

VALID_DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_input() -> list[str]:
    input = []
    with open("input.csv", "r") as file:
        for line in file:
            input.append(str(line).strip())
    
    return input

def solve(input: list[str]) -> int:
    total = 0

    for line in input:
        first = None
        last = None
        for i in range(len(line)):
            if line[i].isdigit():
                if first is None:
                    first = int(line[i])
                else:
                    last = int(line[i])
            else:
                for digit, word in enumerate(VALID_DIGITS, start=1):
                    if line[i:].startswith(word):
                        if first is None:
                            first = digit
                        else:
                            last = digit
        if last is None:
            value = int(f"{first}{first}")
        else:
            value = int(f"{first}{last}")
        
        total += value
    return total

if __name__ == "__main__":
    inputs = get_input()

    print(solve(inputs))