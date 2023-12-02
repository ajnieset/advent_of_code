from solution import get_input


def solve(inputs: dict[int,list[dict]]):
    minimum_colors = {}
    power_sum = 0
    for game_id in inputs.keys():
        minimum_colors[game_id] = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
    for game_id in inputs.keys():
        for color in inputs[game_id]:
            color_name = list(color.keys())[0]
            if color[color_name] > minimum_colors[game_id][color_name]:
                minimum_colors[game_id][color_name] = color[color_name]
    for game_id in minimum_colors.keys():
        power = minimum_colors[game_id]['red'] * minimum_colors[game_id]['blue'] * minimum_colors[game_id]['green']
        power_sum += power
    return power_sum

if __name__ == "__main__":
    inputs = get_input("input.csv")
    print(solve(inputs))