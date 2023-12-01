def get_input() -> list[str]:
    input = []
    with open("input.csv", "r") as file:
        for line in file:
            input.append(str(line).strip())
    
    return input

def solve(input: list[str]) -> int:
    sum = 0

    for line in input:
        first = None
        last = None
        for char in line:
            try:
                int(char)
                temp = str(char)
            except Exception:
                temp = None
            
            if first is None:
                first = temp
            elif last is None or temp is not None:
                last = temp

        if last is None:
            value = int(f"{first}{first}")
        else:
            value = int(f"{first}{last}")

        sum += value

    return sum

if __name__ == "__main__":
    inputs = get_input()
    print(solve(inputs))