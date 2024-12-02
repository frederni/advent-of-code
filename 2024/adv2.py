import numpy as np


def parse_input(file: str = "./inputs/2.txt"):
    with open(file, "r") as f:
        lines = [line.strip() for line in f]
    numbers = [[int(num) for num in x.split()] for x in lines]
    return numbers


def is_safe(sequence) -> bool:
    diff = np.diff(sequence)
    # Check valid increment level
    if np.max(np.abs(diff)) > 3:
        return False
    if (not all([n < 0 for n in diff])) and (not all([n > 0 for n in diff])):
        return False
    return True


def part_1(data):
    valid = 0
    for sequence in data:
        if is_safe(sequence):
            valid += 1
    return valid

def part_2(data):
    valid = 0
    for sequence in data:
        if is_safe(sequence):
            valid += 1
        # Brute force remove one by one
        else:
            for subsequence in [
                sequence[0:i] + sequence[i + 1 :] for i in range(len(sequence))
            ]:
                if is_safe(subsequence):
                    valid += 1
                    break
    return valid


if __name__ == "__main__":
    data = parse_input()
    print("Part 1:", part_1(data), "Part 2:", part_2(data))
