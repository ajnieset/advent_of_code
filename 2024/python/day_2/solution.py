def read_input():
    with open("input.csv", "r") as f:
        return [list(map(lambda x: int(x), line.split())) for line in f]
    

def is_safe(line: list[int]):

    if line[0] > line[1]:
        line.reverse()

    for i in range(len(line)-1):
        step = line[i+1] - line[i]

        if not 1 <= step <= 3:
            return False
    return True
    
def solve():
    inputs = read_input()
    safety_count = 0

    for line in inputs:
        safe = is_safe(line)
                
        if safe:
            safety_count += 1
        # Part 2
        else:
            for level in range(len(line)):
                new_line = line[:level] + line[level + 1:]

                safe = is_safe(new_line)

                if safe:
                    safety_count += 1
                    break

    
    print(f"{safety_count = }")
        

if __name__ == "__main__":
    solve()