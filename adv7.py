def get_card_mapping():
    card_values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    card_values.update({str(i): i for i in range(2, 10)})
    return card_values

def get_rank_mapping():
    return {
        "high card": 0,
        "pair": 1,
        "two pair": 2,
        "three of a kind": 3,
        "full house": 4,
        "four of a kind": 5,
        "five of a kind": 6,
    }


def parse_input(filename):
    hands, bets = [], []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            h, b = line.split()
            hands.append(h)
            bets.append(int(b))
    return hands, bets


def get_type_from_hand(hand: str):
    chrs = set(hand)
    frequency = {chr: hand.count(chr) for chr in chrs}
    largest_value = max(frequency.values())
    largest_keys = [k for k, v in frequency.items() if v == largest_value]

    if largest_value == 5:
        return "five of a kind"
    if largest_value == 4:
        return "four of a kind"
    if largest_value == 3 and 2 in frequency.values():
        return "full house"
    if largest_value == 3:
        return "three of a kind"
    if largest_value == 2 and len(largest_keys) == 2:
        return "two pair"
    if largest_value == 2:
        return "pair"
    return "high card"


def part_1(filename="input7.txt"):
    """
    First segment by hand type and sort by hand value within each hand type
    This is faster than sorting on all hand types
    """
    mapping = get_card_mapping()
    hands_by_type = dict()

    hand_list, bet_list = parse_input(filename)
    for hand, bet in zip(hand_list, bet_list):
        hand_type = get_type_from_hand(hand)
        hands_by_type[hand_type] = hands_by_type.get(hand_type, []) + [[hand, bet]]
    
    # Assign rank for each hand per hand type
    rank_offset = 1
    all_data = []
    for key in sorted(hands_by_type.keys(), key=get_rank_mapping().get):
        hand_data = sorted(
            hands_by_type[key], key=lambda x: [mapping[card] for card in x[0]]
        )
        hand_data_ranked = [d + [idx + rank_offset] for idx, d in enumerate(hand_data)]
        all_data.extend(hand_data_ranked)
        rank_offset = rank_offset + len(hand_data_ranked)

    # Get total winnings
    winnings = sum(hand[1] * hand[2] for hand in all_data)
    return winnings


def part_2():
    pass


if __name__ == "__main__":
    import time

    start_alt1 = time.time()
    for i in range(100):
        answer = part_1("input7.txt")
    end_alt1 = time.time()
    print(f"Time elapsed: {(end_alt1 - start_alt1)*10**6:.2f} us over 100 runs")
    print(answer)
