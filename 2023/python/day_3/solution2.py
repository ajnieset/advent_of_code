from functools import reduce
from solution import get_input, get_positions_to_check

def solve(inputs: list[str]):
    gear_pairs = {}
    line_count = len(inputs)
    ratio_sum = 0
    for line_num, line in enumerate(inputs):
        part_num = ""
        is_gear = False
        for pos, char in enumerate(line):
            if char.isdigit():
                part_num += char

                if is_gear:
                    continue

                checks = get_positions_to_check(line, line_count, line_num, pos)

                for dx, dy in checks:
                    is_gear = inputs[line_num+dy][pos+dx] == "*"
                    star_coord = (line_num+dy, pos+dx)
                    if is_gear:
                        break
                
            else:
                if is_gear:
                    gear_pairs[star_coord] = gear_pairs.get(star_coord, []) + [int(part_num)]
                part_num = ""
                is_gear = False
        if is_gear:
            gear_pairs[star_coord] = gear_pairs.get(star_coord, []) + [int(part_num)]
        
    for coord in gear_pairs:
        if len(gear_pairs[coord]) < 2:
            continue
        ratio_sum += reduce(lambda x, y: x * y, gear_pairs[coord])
    
    return ratio_sum

if __name__ == "__main__":
    inputs = get_input("input.csv")

    print(solve(inputs))