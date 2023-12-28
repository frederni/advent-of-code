def get_input(filename="input4.txt"):
    with open(filename, "r") as f:
        cards = f.readlines()
    return [c.strip() for c in cards]

def parse_numbers(cards):
    def _clean(nums: str) -> list:
        return [int(n) for n in nums.strip().split()]
    winning_numbers = []
    playing_numbers = []
    for card in cards:
        winning, playing = map(_clean, card.split(":")[1].split("|"))
        winning_numbers.append(winning)
        playing_numbers.append(playing)
    return winning_numbers, playing_numbers

def compute_points(winning_list, playing_list) -> int:
    sum_of_points = 0
    assert len(winning_list) == len(playing_list)
    for i in range(len(winning_list)):
        matches = sum([1 for num in playing_list[i] if num in winning_list[i]])
        if matches > 0:
            sum_of_points += 2**(matches-1)
    return sum_of_points

if __name__ == '__main__':
    print(
        compute_points(
            *parse_numbers(
                get_input()
            )
        )
    )