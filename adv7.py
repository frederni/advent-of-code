import time
import timeit


def get_card_mapping(part_2: bool):
    card_values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    card_values.update({str(i): i for i in range(2, 10)})
    if part_2:
        card_values["J"] = 1
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
    with open(filename, "r") as f:
        data = [line.strip().split() for line in f]
    hands, bets = zip(*((h, int(b)) for h, b in data))
    return list(hands), list(bets)


def get_type_from_hand(hand: str, part_2: bool):
    chrs = set(hand)
    if part_2:
        chrs = chrs - {"J"}
        if len(chrs) == 0:  # All Jokers
            return "five of a kind"
    frequency = {chr: hand.count(chr) for chr in chrs}
    largest_value = max(frequency.values())
    largest_keys = [k for k, v in frequency.items() if v == largest_value]
    if part_2:
        jokers = hand.count("J")
        frequency[largest_keys[0]] += jokers
        largest_value += jokers

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


def get_winnings(filename="input7.txt", part_2: bool = False):
    """
    First segment by hand type and sort by hand value within each hand type
    This is faster than sorting on all hand types
    """
    mapping = get_card_mapping(part_2)
    hands_by_type: dict[str, list[tuple[str, int]]] = dict()

    hand_list, bet_list = parse_input(filename)
    for hand, bet in zip(hand_list, bet_list):
        hand_type = get_type_from_hand(hand, part_2)
        hands_by_type[hand_type] = hands_by_type.get(hand_type, []) + [(hand, bet)]

    # Assign rank for each hand per hand type
    rank_offset = 1
    all_data: list[list] = []
    for key in sorted(hands_by_type.keys(), key=get_rank_mapping().get):
        hand_data = sorted(
            hands_by_type[key], key=lambda x: [mapping[card] for card in x[0]]
        )
        hand_data_ranked = [
            list(d) + [idx + rank_offset] for idx, d in enumerate(hand_data)
        ]
        all_data.extend(hand_data_ranked)
        rank_offset = rank_offset + len(hand_data_ranked)

    # Get total winnings
    winnings = sum(hand[1] * hand[2] for hand in all_data)
    return winnings


def performance_test(part_2: bool, n_runs: int = 1000):
    timing = timeit.timeit(
        "get_winnings(part_2=part_2)",
        globals=locals(),
        setup="from __main__ import get_winnings",
        number=n_runs,
    )
    print(f"Part {int(part_2) + 1} took {timing} seconds to run {n_runs} times.")


if __name__ == "__main__":
    print("Part 1", get_winnings())
    print("Part 2", get_winnings(part_2=True))
