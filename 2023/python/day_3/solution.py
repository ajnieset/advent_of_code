POSITIONS = [
    (0, 0),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, 1),
    (0, 1),
    (0, -1),
    (-1, -1)
]

def get_input(filename: str):
    inputs = []
    with open(filename, "r") as file:
        for line in file:
            inputs.append(line.strip())

    return inputs

def get_positions_to_check(line, row_count: int, row: int, col: int) -> list[tuple[int,int]]:
    pos_to_check = []
    if row != 0:
        pos_to_check.append((0, -1))
    if col != 0:
        pos_to_check.append((-1, 0))
    if row != 0 and col != 0:
        pos_to_check.append((-1, -1))
    if row+1 < row_count:
        pos_to_check.append((0, 1))
    if col+1 < len(line):
        pos_to_check.append((1, 0))
    if col+1 < len(line) and row+1 < row_count:
        pos_to_check.append((1, 1))
    if col != 0 and row+1 < row_count:
        pos_to_check.append((-1, 1))
    if col+1 < len(line) and row != 0:
        pos_to_check.append((1, -1))


    return pos_to_check

def solve(inputs: list[str]):
    part_nums = []
    for line_num, line in enumerate(inputs):
        part_num = ""
        is_adjacent = False
        for pos, char in enumerate(line):
            
            if char.isnumeric():
                part_num += char

                if is_adjacent:
                    continue

                pos_to_check = get_positions_to_check(line, len(inputs), line_num, pos)

                for dx, dy in pos_to_check:
                    is_adjacent = not inputs[line_num+dy][pos+dx].isdigit() and inputs[line_num+dy][pos+dx] != "."
                    if is_adjacent:
                        break
            
            else:
                if is_adjacent:
                    part_nums.append(int(part_num))
                part_num = ""
                is_adjacent = False
        if is_adjacent:
            part_nums.append(int(part_num))

    return sum(part_nums)


if __name__ == "__main__":
    inputs = get_input("input.csv")

    print(solve(inputs))