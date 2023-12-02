from solution import solve as part_1

VALID_DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_input() -> list[str]:
    input = []
    with open("input2.csv", "r") as file:
        for line in file:
            input.append(str(line).strip())
    
    return input

def solve(input: list[str]):
    converted = []
    for line in input:
        og_line = line
        first = 9999
        last = -1
        first_word = None
        first_digit = None
        last_word = None
        last_digit = None
        for digit, word in enumerate(VALID_DIGITS, start=1):
            found = line.find(word)
            if first > found and found != -1:
                first = found
                first_word = word
                first_digit = str(digit)
            if last < found:
                last = found
                last_word = word
                last_digit = str(digit)

        if first_word is not None and first_digit is not None:
            line = line.replace(first_word, first_digit)
        if last_word is not None and last_digit is not None:
            line = line.replace(last_word, last_digit)

        for digit, word in enumerate(VALID_DIGITS, start=1):
            line = line.replace(word, str(digit))

        print(f"{og_line = } {line = }")
        converted.append(line)

    return part_1(converted)

if __name__ == "__main__":
    inputs = get_input()

    print(solve(inputs))