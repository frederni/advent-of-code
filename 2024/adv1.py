def parse_input(file: str = "./inputs/1.txt"):
    left_values, right_values = [], []
    with open(file, "r") as f:
        for line in f:
            left, right = line.strip().split(3*" ")
            left_values.append(int(left))
            right_values.append(int(right))
    return left_values, right_values

def part_1(left_values, right_values):
    left, right = sorted(left_values), sorted(right_values)
    distances = [abs(left[i]-right[i]) for i in range(len(left_values))]
    return sum(distances)

def part_2(left_values, right_values):
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
    freq_l = 0
    for number in lv:
        freq_l += number * len([v for v in rv if v == number])
    return freq_l

if __name__ == '__main__':
    print("Part 1:", part_1(*parse_input()))
    print("Part 2:", part_2(*parse_input()))
    
    from utils import test_performance
    test_performance(part_2, part_2_naive, 100, *parse_input())
