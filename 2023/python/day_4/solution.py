def get_input(filename: str):
    inputs = []
    with open(filename, "r") as file:
        for line in file:
            colon = line.find(":") + 1
            inputs.append(line[colon:].strip().split(" | "))
    return inputs


def solve(card_stack: list[list[str]]) -> int:
    total_points = 0

    for card in card_stack:
        card_points = 0
        winning_nums = set(map(int, filter(None, card[0].split(' '))))
        my_nums = set(map(int, filter(None, card[1].split(' '))))

        winners = winning_nums.intersection(my_nums)

        for i in range(len(winners)):
            if i == 0:
                card_points = 1
            else:
                card_points *= 2
        total_points += card_points
    return total_points

if __name__ == "__main__":
    inputs = get_input("input.csv")
    print(solve(inputs))