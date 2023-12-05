def get_input(filename: str):
    inputs = []
    with open(filename, "r") as file:
        for line in file:
            colon = line.find(":") + 1
            inputs.append(line[colon:].strip().split(" | "))
    return inputs


def solve(card_stack: list[list[str]]) -> int:
    card_counts = {}
    total_cards = 0
    stack_size = len(card_stack) + 1

    for card_num, card in enumerate(card_stack, 1):
        card_counts[card_num] = card_counts.get(card_num, 0) + 1
        winning_nums = set(map(int, filter(None, card[0].split(' '))))
        my_nums = set(map(int, filter(None, card[1].split(' '))))

        winners = winning_nums.intersection(my_nums)

        for i in range(1, len(winners)+1):
            if card_num + i < stack_size:
                card_counts[card_num+i] = card_counts.get(card_num+i, 0) + 1 * card_counts[card_num]

    for card_number in card_counts:
        total_cards += card_counts[card_number]

    return total_cards

if __name__ == "__main__":
    inputs = get_input("input.csv")
    print(solve(inputs))