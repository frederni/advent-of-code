import numpy as np

def parse_input(file: str = "./inputs/1.txt"):
    """Parse input. Casts to integer as int comparisons
    will be faster than string comparisons"""
    left_values, right_values = [], []
    with open(file, "r") as f:
        for line in f:
            left, right = line.strip().split(3*" ")
            left_values.append(int(left))
            right_values.append(int(right))
    return left_values, right_values

def part_1(left_values, right_values):
    """Part 1 - sort the lists first then get the absolute difference index by index"""
    left, right = sorted(left_values), sorted(right_values)
    distances = [abs(left[i]-right[i]) for i in range(len(left_values))]
    return sum(distances)

def part_1_np(lv, rv):
    """Equivalent solution in numpy"""
    return np.sum(np.abs(np.sort(lv) - np.sort(rv)))

def part_2(left_values, right_values):
    """Part 2 of the puzzle
    Starts by sorting the left list. We keep record of previous number and its
        frequency in case it's repeated. Only if the value is not seen before, we
        scan the right hand list and get the similarity score
    """
    previous_frequency = 0
    previous_number = None
    frequency_sum = 0
    for number in sorted(left_values):
        if number == previous_number:
            frequency_sum += previous_frequency
        else:
            previous_number = number
            frequency = number * len([v for v in right_values if v==number])
            frequency_sum += frequency
            previous_frequency = frequency
    return frequency_sum

def part_2_naive(lv, rv):
    """A naive implementation of part 2 which scans the right list each time O(n^2)"""
    freq_l = 0
    for number in lv:
        freq_l += number * len([v for v in rv if v == number])
    return freq_l


def part_2_np(lv, rv):
    left = np.array(lv)
    right = np.array(rv)
    unique, counts = np.unique(right, return_counts=True)
    freq_dict = dict(zip(unique, counts))  # Dict/hash map for fast lookup
    return np.sum(left * np.array([freq_dict.get(num, 0) for num in left]))

if __name__ == '__main__':
    left_values, right_values = parse_input()
    print("Part 1:", part_1(left_values, right_values))
    print("Part 2:", part_2(left_values, right_values))

    from utils import test_performance
    print("Part 1 (regular vs numpy):")
    test_performance(part_1, part_1_np, left_values, right_values, n_runs=1000, verbose=True)
    print("Part 1 (regular vs numpy):")
    test_performance(part_2, part_2_np, left_values, right_values, n_runs=100, verbose=True)  
