from math import prod


def parse_input(filename: str = "input6.txt") -> tuple[list[int], list[int]]:
    """Parses input file and returns list for time and record/distance as lists"""
    with open(filename, "r") as f:
        data = f.read().split("\n")
    time = list(map(int, filter(None, data[0].split()[1:])))
    distance = list(map(int, filter(None, data[1].split()[1:])))
    return time, distance


def parse_input_part_2(filename: str = "input6.txt") -> tuple[list[int], list[int]]:
    """Parses input file for part 2 (single race) and returns two single-valued lists"""
    with open(filename, "r") as f:
        data = f.read().split("\n")
    time = int("".join(data[0].split(" ")[1:]))
    distance = int("".join(data[1].split(" ")[1:]))
    return [time], [distance]


def get_distance(time, hold_time):
    """Get's distance based on time and hold time"""
    return hold_time * (time - hold_time)


def main(time: list[int], distance: list[int]):
    """Solves part 1 and 2 of task 6
    The total distance is on form h * (t - h), where t is time and h is hold time
    The optimal hold time is always for h=t/2, so we use binary search to find
    the first hold time that breaks the record. Since the distance is symmetric
    across its apex, the `delta` (the difference between optimal and shortest hold time),
    can be multiplied to get the list of possible hold times. Finally, if `time`
    is even, its optimal time applies for two hold times, so we adjust for this
    using (t+1)%2
    """
    # Solves task for both part 1 and 2
    possible_choices = []
    for t, d in zip(time, distance):
        optimal_hold_time = t // 2
        current_hold_time = optimal_hold_time // 2
        while get_distance(t, current_hold_time) < d:
            current_hold_time = (current_hold_time + optimal_hold_time) // 2

        while get_distance(t, current_hold_time) > d:
            current_hold_time -= 1
        delta = optimal_hold_time - current_hold_time
        possible_choices.append(2 * delta - (t + 1) % 2)
    return prod(possible_choices)


PART_1 = True
PART_2 = True
if __name__ == "__main__":
    if PART_1:
        time, distance = parse_input()
        print(f"Part 1: {main(time, distance)}")
    if PART_2:
        time, distance = parse_input_part_2()
        print(f"Part 2: {main(time, distance)}")
