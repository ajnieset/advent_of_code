import copy


MAX_COLORS = {'red': 12, 'green': 13, 'blue': 14}

def get_input(filename: str) -> dict[int,list[dict[str,int]]]:
    inputs:dict[int, list] = {}
    with open(filename, "r") as file:
        for line in file:
            start = line.find(':') + 1
            game = line[start:]
            draws = game.strip().split(';')
            inputs.update(
                {
                    int(line[5:start-1]): []
                }
            )
            for draw in draws:
                dice = draw.strip().split(',')
                for color in dice:
                    value = color.strip().split(' ')
                    inputs[int(line[5:start-1])].append(
                        {
                            value[1]: int(value[0])
                        }
                    )
    return inputs

def solve(inputs: dict[int,list[dict[str,int]]]):
    games = copy.deepcopy(inputs)
    for game_id in inputs.keys():
        for color in inputs[game_id]:
            color_name = list(color.keys())[0]
            if color[color_name] > MAX_COLORS[color_name]:
                games.pop(game_id)
                break
    return sum(games.keys())

if __name__ == "__main__":
    inputs = get_input("input.csv")
    print(f"solution = {solve(inputs)}")